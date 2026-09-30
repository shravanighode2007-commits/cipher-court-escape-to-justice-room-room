using UnityEngine;
using UnityEngine.SceneManagement;
using TMPro;

public class Level5CasePuzzle : MonoBehaviour
{
    [Header("Puzzle Settings")]
    public string correctCode = "315";

    [Header("Evidence System")]
    public TMP_Text evidenceText;
    private string file1 = "?";
    private string file2 = "?";
    private string file3 = "?";

    [Header("Puzzle UI")]
    public GameObject puzzlePanel;
    public TMP_InputField codeInput;
    public TMP_Text messageText;

    [Header("Timer")]
    public TMP_Text timerText;
    public float levelTime = 300f;
    public float overtimeExtension = 60f;

    [Header("Attempts")]
    public TMP_Text attemptsText;
    public int maxAttempts = 3;

    [Header("Level Failed")]
    public GameObject levelFailedPanel;

    [Header("Door")]
    public GameObject exitDoor;
    public float doorOpenHeight = 4f;
    public float doorOpenSpeed = 2f;

    private float timeRemaining;
    private int attemptsRemaining;
    private bool puzzleSolved = false;
    public bool IsSolved => puzzleSolved;
    private bool levelFailed = false;
    private bool openingDoor = false;
    private Vector3 doorOpenPosition;

    void Start()
    {
        timeRemaining = levelTime;
        attemptsRemaining = maxAttempts;
        if (puzzlePanel != null) puzzlePanel.SetActive(false);
        if (levelFailedPanel != null) levelFailedPanel.SetActive(false);
        if (exitDoor != null) doorOpenPosition = exitDoor.transform.position + Vector3.up * doorOpenHeight;
        if (messageText != null) messageText.text = "";
        UpdateEvidenceText();
        UpdateTimer();
        UpdateAttempts();
    }

    void Update()
    {
        if (!puzzleSolved && !levelFailed)
        {
            timeRemaining -= Time.deltaTime;
            if (timeRemaining <= 0f) ApplyTimePenalty();
            UpdateTimer();
        }

        if (openingDoor && exitDoor != null)
        {
            exitDoor.transform.position = Vector3.MoveTowards(
                exitDoor.transform.position, doorOpenPosition, doorOpenSpeed * Time.deltaTime);
            if (Vector3.Distance(exitDoor.transform.position, doorOpenPosition) < 0.01f)
            {
                exitDoor.transform.position = doorOpenPosition;
                openingDoor = false;
            }
        }
    }

    void ApplyTimePenalty()
    {
        timeRemaining = Mathf.Max(30f, overtimeExtension);
        PopupFeedback.Show("TIME EXPIRED - CASE REVIEW PENALTY\n+60 SECONDS", false, 2.4f);
        CipherCourtDatabase.LogEvent("time_penalty", "penalty", "Level 5 extra time granted");
    }

    public void CollectFile(int fileNumber, string value)
    {
        if (puzzleSolved || levelFailed) return;
        if (fileNumber == 1) file1 = value;
        else if (fileNumber == 2) file2 = value;
        else if (fileNumber == 3) file3 = value;
        UpdateEvidenceText();
    }

    void UpdateEvidenceText()
    {
        if (evidenceText != null)
            evidenceText.text = "CASE FILE CODE\n" + file1 + " - " + file2 + " - " + file3;
    }

    public void OpenPuzzle()
    {
        if (puzzleSolved || levelFailed) return;
        if (puzzlePanel != null) puzzlePanel.SetActive(true);
        if (messageText != null) messageText.text = "ENTER CASE FILE CODE";
        if (codeInput != null)
        {
            codeInput.text = "";
            codeInput.Select();
            codeInput.ActivateInputField();
        }
        Cursor.lockState = CursorLockMode.None;
        Cursor.visible = true;
    }

    public void ClosePuzzle()
    {
        if (puzzlePanel != null) puzzlePanel.SetActive(false);
        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
    }

    public void CheckCode()
    {
        if (puzzleSolved || levelFailed || codeInput == null) return;
        string enteredCode = codeInput.text.Trim();

        if (enteredCode == correctCode)
        {
            PopupFeedback.Show("CORRECT ANSWER - CASE VERIFIED", true);
            CipherCourtDatabase.LogEvent("puzzle_answer", "correct", "Level 5 case code solved");
            PuzzleSolved();
        }
        else
        {
            attemptsRemaining--;
            UpdateAttempts();
            PopupFeedback.Show("INCORRECT ANSWER - TRY AGAIN", false);
            CipherCourtDatabase.LogEvent("puzzle_answer", "incorrect", "Wrong Level 5 code");

            if (attemptsRemaining <= 0)
            {
                FailLevel();
                return;
            }

            if (messageText != null)
                messageText.text = "WRONG CODE! ATTEMPTS LEFT: " + attemptsRemaining;
            codeInput.text = "";
            codeInput.Select();
            codeInput.ActivateInputField();
        }
    }

    void PuzzleSolved()
    {
        puzzleSolved = true;
        if (messageText != null) messageText.text = "CASE VERIFIED";
        openingDoor = true;
        Invoke(nameof(ClosePuzzle), 1.5f);
    }

    void UpdateTimer()
    {
        if (timerText == null) return;
        int minutes = Mathf.FloorToInt(timeRemaining / 60f);
        int seconds = Mathf.FloorToInt(timeRemaining % 60f);
        timerText.text = minutes.ToString("00") + ":" + seconds.ToString("00");
    }

    void UpdateAttempts()
    {
        if (attemptsText != null) attemptsText.text = "ATTEMPTS: " + attemptsRemaining;
    }

    void FailLevel()
    {
        if (levelFailed) return;
        levelFailed = true;
        if (puzzlePanel != null) puzzlePanel.SetActive(false);
        if (levelFailedPanel != null) levelFailedPanel.SetActive(true);
        Cursor.lockState = CursorLockMode.None;
        Cursor.visible = true;
        CipherCourtDatabase.LogEvent("level_failed", "failed", "Level 5 attempts exhausted");
    }

    public void RetryLevel() => SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    public void MainMenu() => SceneManager.LoadScene("MainMenu");
}
