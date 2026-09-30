using System.Collections;
using UnityEngine;
using UnityEngine.EventSystems;
using TMPro;

public class PasswordPuzzleUI : MonoBehaviour
{
    [SerializeField] private GameObject puzzlePanel;
    [SerializeField] private TMP_InputField answerInput;
    [SerializeField] private TMP_Text feedbackText;
    [SerializeField] private PasswordPuzzle passwordPuzzle;

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
        puzzlePanel.SetActive(true);

        if (playerMovement != null)
            playerMovement.enabled = false;

        if (mouseLook != null)
            mouseLook.enabled = false;

        Cursor.lockState = CursorLockMode.None;
        Cursor.visible = true;

        answerInput.text = "";
        feedbackText.text = "";

        StartCoroutine(FocusInput());
    }

    private IEnumerator FocusInput()
    {
        yield return null;

        if (EventSystem.current != null)
            EventSystem.current.SetSelectedGameObject(answerInput.gameObject);

        answerInput.Select();
        answerInput.ActivateInputField();
    }

    public void SubmitAnswer()
    {
        bool correct = passwordPuzzle.CheckAnswer(answerInput.text);

        if (correct)
        {
            feedbackText.text = "CORRECT! DOOR UNLOCKED.";
            PopupFeedback.Show("CORRECT ANSWER - ACCESS GRANTED", true);
            CipherCourtDatabase.LogEvent("puzzle_answer", "correct", "Password puzzle solved");
            Invoke(nameof(ClosePuzzle), 1f);
        }
        else
        {
            feedbackText.text = "WRONG PASSWORD. TRY AGAIN.";
            PopupFeedback.Show("INCORRECT ANSWER - TRY AGAIN", false);
            CipherCourtDatabase.LogEvent("puzzle_answer", "incorrect", "Wrong password entered");
            StartCoroutine(FocusInput());
        }
    }

    public void ClosePuzzle()
    {
        puzzlePanel.SetActive(false);

        if (playerMovement != null)
            playerMovement.enabled = true;

        if (mouseLook != null)
            mouseLook.enabled = true;

        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
    }
}