using System.Collections;
using UnityEngine;
using UnityEngine.EventSystems;
using TMPro;

public class PuzzleUI : MonoBehaviour
{
    [SerializeField] private GameObject puzzlePanel;
    [SerializeField] private TMP_InputField answerInput;
    [SerializeField] private TMP_Text feedbackText;
    [SerializeField] private CipherPuzzle cipherPuzzle;

    [SerializeField] private PlayerMovement playerMovement;
    [SerializeField] private MouseLook mouseLook;

    private void Start()
    {
        feedbackText.text = "";
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

        StartCoroutine(FocusInputField());
    }

    private IEnumerator FocusInputField()
    {
        yield return null;

        EventSystem.current.SetSelectedGameObject(answerInput.gameObject);
        answerInput.Select();
        answerInput.ActivateInputField();
    }

    public void SubmitAnswer()
    {
        bool correct = cipherPuzzle.CheckAnswer(answerInput.text);

        if (correct)
        {
            feedbackText.text = "Correct! Door Unlocked.";
            PopupFeedback.Show("CORRECT ANSWER - DOOR UNLOCKED", true);
            CipherCourtDatabase.LogEvent("puzzle_answer", "correct", "Cipher puzzle solved");

            ClosePuzzle();
        }
        else
        {
            feedbackText.text = "Wrong answer. Try again.";
            PopupFeedback.Show("INCORRECT ANSWER - TRY AGAIN", false);
            CipherCourtDatabase.LogEvent("puzzle_answer", "incorrect", "Wrong cipher answer entered");
            StartCoroutine(FocusInputField());
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