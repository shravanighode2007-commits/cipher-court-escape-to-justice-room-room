using System.Collections;
using UnityEngine;
using UnityEngine.EventSystems;
using TMPro;

public class EvidencePuzzleUI : MonoBehaviour
{
    [SerializeField] private GameObject puzzlePanel;
    [SerializeField] private TMP_InputField answerInput;
    [SerializeField] private TMP_Text feedbackText;
    [SerializeField] private EvidencePuzzle evidencePuzzle;

    [Header("Player Controls")]
    [SerializeField] private PlayerMovement playerMovement;
    [SerializeField] private MouseLook mouseLook;

    private void Start()
    {
        if (feedbackText != null)
            feedbackText.text = "";

        if (puzzlePanel != null)
            puzzlePanel.SetActive(false);
    }

    public void OpenPuzzle()
    {
        if (puzzlePanel != null)
            puzzlePanel.SetActive(true);

        if (playerMovement != null)
            playerMovement.enabled = false;

        if (mouseLook != null)
            mouseLook.enabled = false;

        Cursor.lockState = CursorLockMode.None;
        Cursor.visible = true;

        if (answerInput != null)
            answerInput.text = "";

        if (feedbackText != null)
            feedbackText.text = "";

        StartCoroutine(FocusInput());
    }

    private IEnumerator FocusInput()
    {
        yield return null;

        if (answerInput == null)
            yield break;

        if (EventSystem.current != null)
            EventSystem.current.SetSelectedGameObject(answerInput.gameObject);

        answerInput.Select();
        answerInput.ActivateInputField();
    }

    public void SubmitAnswer()
    {
        if (evidencePuzzle == null || answerInput == null)
            return;

        bool correct = evidencePuzzle.CheckAnswer(answerInput.text);

        if (correct)
        {
            if (feedbackText != null)
                feedbackText.text = "CORRECT! DOOR UNLOCKED.";
                PopupFeedback.Show("CORRECT ANSWER - EVIDENCE VERIFIED", true);
                CipherCourtDatabase.LogEvent("puzzle_answer", "correct", "Evidence puzzle solved");

            Invoke(nameof(ClosePuzzle), 1f);
        }
        else
        {
            if (feedbackText != null)
                feedbackText.text = "WRONG CODE. TRY AGAIN.";
                PopupFeedback.Show("INCORRECT ANSWER - TRY AGAIN", false);
                CipherCourtDatabase.LogEvent("puzzle_answer", "incorrect", "Wrong evidence code entered");

            StartCoroutine(FocusInput());
        }
    }

    public void ClosePuzzle()
    {
        if (puzzlePanel != null)
            puzzlePanel.SetActive(false);

        if (playerMovement != null)
            playerMovement.enabled = true;

        if (mouseLook != null)
            mouseLook.enabled = true;

        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
    }
}