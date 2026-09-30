using UnityEngine;
using UnityEngine.InputSystem;
using TMPro;

public class ArchiveKeypad : MonoBehaviour
{
    public Level4ArchivePuzzle puzzle;
    public TMP_Text interactionText;

    private bool playerNearby = false;

    void Update()
    {
        if (playerNearby &&
            Keyboard.current != null &&
            Keyboard.current.eKey.wasPressedThisFrame)
        {
            Debug.Log("E PRESSED AT KEYPAD");

            if (puzzle != null)
            {
                puzzle.OpenKeypad();
            }
            else
            {
                Debug.LogError("PUZZLE IS NOT ASSIGNED!");
            }
        }
    }

    void OnTriggerEnter(Collider other)
    {
        Debug.Log("KEYPAD TRIGGER ENTERED BY: " + other.name);

        if (other.CompareTag("Player") ||
            other.transform.root.CompareTag("Player"))
        {
            playerNearby = true;

            Debug.Log("PLAYER NEAR KEYPAD");

            if (interactionText != null)
            {
                interactionText.text = "Press E to use keypad";
                interactionText.gameObject.SetActive(true);
            }
        }
    }

    void OnTriggerExit(Collider other)
    {
        if (other.CompareTag("Player") ||
            other.transform.root.CompareTag("Player"))
        {
            playerNearby = false;

            if (interactionText != null)
                interactionText.gameObject.SetActive(false);
        }
    }
}