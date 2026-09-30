using UnityEngine;
using UnityEngine.InputSystem;

public class PuzzleInteraction : MonoBehaviour
{
    [SerializeField] private PuzzleUI puzzleUI;
    [SerializeField] private Transform player;
    [SerializeField] private GameObject interactionText;
    [SerializeField] private GameObject requirementText;
    [SerializeField] private float interactionDistance = 3f;

    private bool puzzleOpen = false;
    private Level1Progress progress;

    private void Start()
    {
        if (player != null)
        {
            progress = player.GetComponent<Level1Progress>();
        }

        if (interactionText != null)
            interactionText.SetActive(false);

        if (requirementText != null)
            requirementText.SetActive(false);
    }

    private void Update()
    {
        if (player == null || puzzleUI == null || progress == null)
            return;

        float distance = Vector3.Distance(
            player.position,
            transform.position
        );

        bool playerIsNear = distance <= interactionDistance;

        // Show "Press E" when player is near
        if (interactionText != null)
        {
            interactionText.SetActive(
                playerIsNear && !puzzleOpen
            );
        }

        // Press E to interact
        if (playerIsNear &&
            !puzzleOpen &&
            Keyboard.current != null &&
            Keyboard.current.eKey.wasPressedThisFrame)
        {
            // Player must collect BOTH items first
            if (!progress.HasClue || !progress.HasKey)
            {
                if (requirementText != null)
                {
                    requirementText.SetActive(true);

                    CancelInvoke(nameof(HideRequirementText));
                    Invoke(nameof(HideRequirementText), 2f);
                }

                return;
            }

            // Both collected — open puzzle
            puzzleOpen = true;

            if (interactionText != null)
                interactionText.SetActive(false);

            if (requirementText != null)
                requirementText.SetActive(false);

            puzzleUI.OpenPuzzle();
        }
    }

    private void HideRequirementText()
    {
        if (requirementText != null)
        {
            requirementText.SetActive(false);
        }
    }

    public void PuzzleClosed()
    {
        puzzleOpen = false;
    }
}