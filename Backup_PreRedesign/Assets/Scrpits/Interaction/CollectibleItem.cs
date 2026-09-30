using UnityEngine;
using UnityEngine.InputSystem;

public class CollectibleItem : MonoBehaviour
{
    public enum ItemType
    {
        Clue,
        Key
    }

    [SerializeField] private ItemType itemType;

    private Vector3 initialPos;
    private bool collected = false;
    private bool playerNearby = false;

    private void Start()
    {
        initialPos = transform.position;

        // Ensure trigger collider exists with generous radius
        SphereCollider col = GetComponent<SphereCollider>();
        if (col == null) col = gameObject.AddComponent<SphereCollider>();
        col.isTrigger = true;
        col.radius = 2.2f;

        // Ensure kinematic Rigidbody so Unity 3D physics always triggers events
        Rigidbody rb = GetComponent<Rigidbody>();
        if (rb == null) rb = gameObject.AddComponent<Rigidbody>();
        rb.isKinematic = true;
        rb.useGravity = false;
    }

    private void Update()
    {
        if (collected) return;

        // Visual bobbing and gentle spinning animation
        float newY = initialPos.y + Mathf.Sin(Time.time * 2.5f) * 0.08f;
        transform.position = new Vector3(initialPos.x, newY, initialPos.z);
        transform.Rotate(Vector3.up, 35f * Time.deltaTime, Space.World);

        // Input collection fallback when player is nearby or pressing E
        bool ePressed = false;
        try { if (Input.GetKeyDown(KeyCode.E)) ePressed = true; } catch {}
        try { if (Keyboard.current != null && Keyboard.current.eKey.wasPressedThisFrame) ePressed = true; } catch {}

        if (playerNearby && ePressed)
        {
            Collect();
        }
    }

    private void OnTriggerEnter(Collider other)
    {
        if (IsPlayer(other))
        {
            playerNearby = true;
            // Immediate collection on touch as primary mechanism
            Collect();
        }
    }

    private void OnTriggerStay(Collider other)
    {
        if (!collected && IsPlayer(other))
        {
            playerNearby = true;
            Collect();
        }
    }

    private void OnTriggerExit(Collider other)
    {
        if (IsPlayer(other))
        {
            playerNearby = false;
        }
    }

    private void Collect()
    {
        if (collected) return;
        collected = true;

        Level1Progress progress = FindFirstObjectByType<Level1Progress>();

        if (progress != null)
        {
            if (itemType == ItemType.Clue)
            {
                progress.CollectClue();
                PopupFeedback.Show("INVESTIGATION CLUE COLLECTED!", true);
                CipherCourtDatabase.LogEvent("clue_collected", "success", "Level 1 Investigation Clue");
            }
            else if (itemType == ItemType.Key)
            {
                progress.CollectKey();
                PopupFeedback.Show("SECURITY KEY COLLECTED!", true);
                CipherCourtDatabase.LogEvent("clue_collected", "success", "Level 1 Security Key");
            }
        }

        // Clean up linked beacon light if any exists
        CleanUpBeacon();

        Destroy(gameObject);
    }

    private void CleanUpBeacon()
    {
        GameObject root = GameObject.Find("_VISUAL_POLISH_V13_");
        if (root != null)
        {
            foreach (Transform child in root.transform)
            {
                if (child.name.StartsWith("ClueBeacon_") && Vector3.Distance(child.position, transform.position) < 2.5f)
                {
                    Destroy(child.gameObject);
                }
            }
        }
    }

    private bool IsPlayer(Collider other)
    {
        if (other == null) return false;
        if (other.CompareTag("Player") || other.transform.root.CompareTag("Player")) return true;
        if (other.GetComponentInParent<CharacterController>() != null) return true;
        if (other.name.ToLower().Contains("player")) return true;
        return false;
    }
}