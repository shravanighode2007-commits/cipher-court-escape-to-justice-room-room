using UnityEngine;
using UnityEngine.InputSystem;
using TMPro;

public class Level5Terminal : MonoBehaviour
{
    [Header("Puzzle")]
    public Level5CasePuzzle puzzle;

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
                puzzle.OpenPuzzle();

                if (interactionText != null)
                    interactionText.gameObject.SetActive(false);
            }
            else
            {
                Debug.LogError(
                    "Level5CasePuzzle is not assigned!"
                );
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
                    "Press E to use case terminal";

                interactionText.gameObject.SetActive(true);
            }

            Debug.Log("PLAYER NEAR CASE TERMINAL");
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