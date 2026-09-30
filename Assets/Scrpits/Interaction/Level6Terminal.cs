using UnityEngine;
using UnityEngine.InputSystem;
using TMPro;

public class Level6Terminal : MonoBehaviour
{
    [Header("Puzzle")]
    public Level6VerdictPuzzle puzzle;

    [Header("UI")]
    public TMP_Text interactionText;

    private bool playerNearby = false;

    void Start()
    {
        if (interactionText != null)
            interactionText.gameObject.SetActive(false);
    }

    void Update()
    {
        if (playerNearby &&
            Keyboard.current != null &&
            Keyboard.current.eKey.wasPressedThisFrame)
        {
            if (puzzle != null)
            {
                puzzle.OpenVerdictPanel();

                if (interactionText != null)
                    interactionText.gameObject.SetActive(false);
            }
            else
            {
                Debug.LogError("Level6VerdictPuzzle not assigned!");
            }
        }
    }

    void OnTriggerEnter(Collider other)
    {
        if (IsPlayer(other))
        {
            playerNearby = true;

            if (interactionText != null)
            {
                interactionText.text =
                    "Press E to give your verdict";

                interactionText.gameObject.SetActive(true);
            }
        }
    }

    void OnTriggerExit(Collider other)
    {
        if (IsPlayer(other))
        {
            playerNearby = false;

            if (interactionText != null)
                interactionText.gameObject.SetActive(false);
        }
    }

    bool IsPlayer(Collider other)
    {
        if (other.CompareTag("Player"))
            return true;

        if (other.transform.root.CompareTag("Player"))
            return true;

        return false;
    }
}