using UnityEngine;
using UnityEngine.SceneManagement;
using TMPro;

public class Level4ArchivePuzzle : MonoBehaviour
{
    [Header("Puzzle Settings")]
    public string correctCode = "427";

    [Header("Clue System")]
    public TMP_Text clueDisplayText;
    private string clue1 = "?";
    private string clue2 = "?";
    private string clue3 = "?";

    [Header("Keypad UI")]
    public GameObject keypadPanel;
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

    [Header("Door Movement")]
    public Vector3 doorOpenOffset = new Vector3(0, 3f, 0);
    public float doorOpenSpeed = 2f;

    private float timeRemaining;
    private int attemptsRemaining;
    private Vector3 openPosition;
    private bool puzzleSolved = false;
    public bool IsSolved => puzzleSolved;
    private bool openingDoor = false;
    private bool levelFailed = false;

    void Start()
    {
        timeRemaining = levelTime;
        attemptsRemaining = maxAttempts;
        if (keypadPanel != null) keypadPanel.SetActive(false);
        if (levelFailedPanel != null) levelFailedPanel.SetActive(false);
        if (exitDoor != null) openPosition = exitDoor.transform.position + doorOpenOffset;
        if (messageText != null) messageText.text = "";
        UpdateClueDisplay();
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
                exitDoor.transform.position, openPosition, doorOpenSpeed * Time.deltaTime);
            if (Vector3.Distance(exitDoor.transform.position, openPosition) < 0.01f)
                openingDoor = false;
        }
    }

    void ApplyTimePenalty()
    {
        timeRemaining = Mathf.Max(30f, overtimeExtension);
        PopupFeedback.Show("TIME EXPIRED - ARCHIVE PENALTY\n+60 SECONDS", false, 2.4f);
        CipherCourtDatabase.LogEvent("time_penalty", "penalty", "Level 4 extra time granted");
    }

    public void CollectClue(int clueNumber, string clueValue)
    {
        if (puzzleSolved || levelFailed) return;
        if (clueNumber == 1) clue1 = clueValue;
        else if (clueNumber == 2) clue2 = clueValue;
        else if (clueNumber == 3) clue3 = clueValue;
        UpdateClueDisplay();
    }

    void UpdateClueDisplay()
    {
        if (clueDisplayText != null)
            clueDisplayText.text = "ARCHIVE CODE\n" + clue1 + " - " + clue2 + " - " + clue3;
    }

    public void OpenKeypad()
    {
        if (puzzleSolved || levelFailed) return;
        if (keypadPanel != null) keypadPanel.SetActive(true);
        if (messageText != null) messageText.text = "ENTER ARCHIVE CODE";
        if (codeInput != null)
        {
            codeInput.text = "";
            codeInput.Select();
            codeInput.ActivateInputField();
        }
        Cursor.lockState = CursorLockMode.None;
        Cursor.visible = true;
    }

    public void CloseKeypad()
    {
        if (keypadPanel != null) keypadPanel.SetActive(false);
        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
    }

    public void CheckCode()
    {
        if (puzzleSolved || levelFailed || codeInput == null) return;

        if (codeInput.text.Trim() == correctCode)
        {
            PopupFeedback.Show("CORRECT CODE - ARCHIVE ACCESS GRANTED", true);
            CipherCourtDatabase.LogEvent("puzzle_answer", "correct", "Archive code solved");
            PuzzleSolved();
        }
        else
        {
            attemptsRemaining--;
            UpdateAttempts();
            PopupFeedback.Show("INCORRECT CODE - TRY AGAIN", false);
            CipherCourtDatabase.LogEvent("puzzle_answer", "incorrect", "Wrong archive code");

            if (attemptsRemaining <= 0)
            {
                FailLevel();
                return;
            }

            if (messageText != null)
                messageText.text = "WRONG CODE! ATTEMPTS LEFT: " + attemptsRemaining;
            codeInput.text = "";
        }
    }

    void PuzzleSolved()
    {
        puzzleSolved = true;
        if (messageText != null) messageText.text = "ACCESS GRANTED";
        openingDoor = true;
        Invoke(nameof(CloseKeypad), 1.5f);
    }

    void FailLevel()
    {
        if (levelFailed) return;
        levelFailed = true;
        if (keypadPanel != null) keypadPanel.SetActive(false);
        if (levelFailedPanel != null) levelFailedPanel.SetActive(true);
        Cursor.lockState = CursorLockMode.None;
        Cursor.visible = true;
        CipherCourtDatabase.LogEvent("level_failed", "failed", "Level 4 attempts exhausted");
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

    public void RetryLevel() => SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    public void MainMenu() => SceneManager.LoadScene("MainMenu");
}
