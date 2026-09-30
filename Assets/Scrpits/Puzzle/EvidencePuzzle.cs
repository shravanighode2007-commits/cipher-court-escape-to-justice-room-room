using UnityEngine;
using TMPro;

public class EvidencePuzzle : MonoBehaviour
{
    [Header("Puzzle")]
    [SerializeField] private string correctAnswer = "472";

    [Header("Door")]
    [SerializeField] private GameObject door;
    [SerializeField] private float doorOpenHeight = 4f;
    [SerializeField] private float doorOpenSpeed = 2f;

    [Header("Attempts")]
    [SerializeField] private int maxAttempts = 3;
    [SerializeField] private TMP_Text attemptsText;

    [Header("Timer")]
    [SerializeField] private LevelTimer levelTimer;

    private int attemptsRemaining;
    private bool solved = false;
    public bool IsSolved => solved;

    // Door movement
    private Vector3 doorOpenPosition;
    private bool openingDoor = false;


    private void Start()
    {
        // Setup attempts
        attemptsRemaining = maxAttempts;
        UpdateAttemptsText();

        // Calculate where the door should move
        if (door != null)
        {
            doorOpenPosition =
                door.transform.position +
                Vector3.up * doorOpenHeight;
        }
    }


    private void Update()
    {
        // Move door upward
        if (openingDoor && door != null)
        {
            door.transform.position =
                Vector3.MoveTowards(
                    door.transform.position,
                    doorOpenPosition,
                    doorOpenSpeed * Time.deltaTime
                );

            // Stop when door reaches target position
            if (Vector3.Distance(
                door.transform.position,
                doorOpenPosition) < 0.01f)
            {
                door.transform.position = doorOpenPosition;

                openingDoor = false;
            }
        }
    }


    public bool CheckAnswer(string playerAnswer)
    {
        // Puzzle already solved
        if (solved)
            return true;


        // ==========================================
        // CORRECT ANSWER
        // ==========================================

        if (playerAnswer.Trim() == correctAnswer)
        {
            solved = true;

            // Open door upward
            OpenDoor();

            // Stop timer
            if (levelTimer != null)
            {
                levelTimer.StopTimer();
            }

            Debug.Log(
                "Evidence puzzle solved. Door opening upward."
            );

            return true;
        }


        // ==========================================
        // WRONG ANSWER
        // ==========================================

        attemptsRemaining--;

        UpdateAttemptsText();

        Debug.Log(
            "Wrong answer. Attempts left: " +
            attemptsRemaining
        );


        // No attempts remaining
        if (attemptsRemaining <= 0)
        {
            if (levelTimer != null)
            {
                levelTimer.FailLevel();
            }
        }

        return false;
    }


    // ==============================================
    // OPEN DOOR
    // ==============================================

    private void OpenDoor()
    {
        if (door == null)
        {
            Debug.LogError(
                "Door is not assigned in EvidencePuzzle!"
            );

            return;
        }

        openingDoor = true;
    }


    // ==============================================
    // UPDATE ATTEMPTS
    // ==============================================

    private void UpdateAttemptsText()
    {
        if (attemptsText != null)
        {
            attemptsText.text =
                "ATTEMPTS: " +
                attemptsRemaining;
        }
    }
}