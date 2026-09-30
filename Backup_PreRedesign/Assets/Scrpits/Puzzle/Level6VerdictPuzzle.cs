using UnityEngine;
using UnityEngine.SceneManagement;
using TMPro;

public class Level6VerdictPuzzle : MonoBehaviour
{
    [Header("Puzzle Settings")]
    public int correctStatement = 2;

    [Header("Statement UI")]
    public TMP_Text statementText;

    [Header("Verdict Panel")]
    public GameObject verdictPanel;
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
        if (verdictPanel != null) verdictPanel.SetActive(false);
        if (levelFailedPanel != null) levelFailedPanel.SetActive(false);
        if (exitDoor != null) doorOpenPosition = exitDoor.transform.position + Vector3.up * doorOpenHeight;
        if (statementText != null) statementText.text = "INSPECT THE WITNESS STATEMENTS";
        if (messageText != null) messageText.text = "";
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
        PopupFeedback.Show("TIME EXPIRED - COURT PENALTY\n+60 SECONDS", false, 2.4f);
        CipherCourtDatabase.LogEvent("time_penalty", "penalty", "Level 6 extra time granted");
    }

    public void ShowStatement(int statementNumber)
    {
        if (puzzleSolved || levelFailed || statementText == null) return;
        if (statementNumber == 1)
            statementText.text = "STATEMENT 1\n\n\"The suspect entered at 8 PM.\"";
        else if (statementNumber == 2)
            statementText.text = "STATEMENT 2\n\n\"The security camera was working.\"";
        else if (statementNumber == 3)
            statementText.text = "STATEMENT 3\n\n\"The camera footage shows no entry.\"";
    }

    public void OpenVerdictPanel()
    {
        if (puzzleSolved || levelFailed) return;
        if (verdictPanel != null) verdictPanel.SetActive(true);
        if (messageText != null) messageText.text = "SELECT THE FALSE STATEMENT";
        Cursor.lockState = CursorLockMode.None;
        Cursor.visible = true;
    }

    public void CloseVerdictPanel()
    {
        if (verdictPanel != null) verdictPanel.SetActive(false);
        Cursor.lockState = CursorLockMode.Locked;
        Cursor.visible = false;
    }

    public void ChooseStatement(int statementNumber)
    {
        if (puzzleSolved || levelFailed) return;

        if (statementNumber == correctStatement)
        {
            PopupFeedback.Show("CORRECT VERDICT - JUSTICE SERVED", true);
            CipherCourtDatabase.LogEvent("puzzle_answer", "correct", "Final verdict solved");
            PuzzleSolved();
        }
        else
        {
            attemptsRemaining--;
            UpdateAttempts();
            PopupFeedback.Show("INCORRECT VERDICT - REVIEW THE EVIDENCE", false);
            CipherCourtDatabase.LogEvent("puzzle_answer", "incorrect", "Wrong final verdict");

            if (attemptsRemaining <= 0)
            {
                FailLevel();
                return;
            }
            if (messageText != null)
                messageText.text = "WRONG VERDICT! ATTEMPTS LEFT: " + attemptsRemaining;
        }
    }

    void PuzzleSolved()
    {
        puzzleSolved = true;
        if (messageText != null) messageText.text = "CORRECT VERDICT";
        openingDoor = true;
        Invoke(nameof(CloseVerdictPanel), 1.5f);
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
        if (verdictPanel != null) verdictPanel.SetActive(false);
        if (levelFailedPanel != null) levelFailedPanel.SetActive(true);
        Cursor.lockState = CursorLockMode.None;
        Cursor.visible = true;
        CipherCourtDatabase.LogEvent("level_failed", "failed", "Level 6 attempts exhausted");
    }

    public void RetryLevel() => SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    public void MainMenu() => SceneManager.LoadScene("MainMenu");
}
