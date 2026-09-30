using System.Collections;
using TMPro;
using UnityEngine;
using UnityEngine.UI;

public class PopupFeedback : MonoBehaviour
{
    private static PopupFeedback instance;
    private Canvas canvas;
    private Image panelBg;
    private Image panelBorder;
    private TMP_Text titleText;
    private TMP_Text subText;
    private CanvasGroup canvasGroup;
    private RectTransform panelRect;
    private Coroutine routine;

    [RuntimeInitializeOnLoadMethod(RuntimeInitializeLoadType.AfterSceneLoad)]
    private static void Bootstrap()
    {
        if (instance != null) return;
        GameObject go = new GameObject("PopupFeedbackSystem");
        instance = go.AddComponent<PopupFeedback>();
        DontDestroyOnLoad(go);
        instance.BuildUI();
    }

    private void BuildUI()
    {
        canvas = gameObject.AddComponent<Canvas>();
        canvas.renderMode = RenderMode.ScreenSpaceOverlay;
        canvas.sortingOrder = 9000;
        var scaler = gameObject.AddComponent<CanvasScaler>();
        scaler.uiScaleMode = CanvasScaler.ScaleMode.ScaleWithScreenSize;
        scaler.referenceResolution = new Vector2(1920, 1080);
        scaler.matchWidthOrHeight = 0.5f;
        gameObject.AddComponent<GraphicRaycaster>();

        GameObject panelGO = new GameObject("PopupPanel");
        panelGO.transform.SetParent(transform, false);
        canvasGroup = panelGO.AddComponent<CanvasGroup>();
        panelRect = panelGO.AddComponent<RectTransform>();
        panelRect.anchorMin = new Vector2(0.5f, 0.88f);
        panelRect.anchorMax = new Vector2(0.5f, 0.88f);
        panelRect.pivot = new Vector2(0.5f, 0.5f);
        panelRect.sizeDelta = new Vector2(520f, 90f);

        // Border image
        panelBorder = panelGO.AddComponent<Image>();
        panelBorder.color = new Color(0.95f, 0.82f, 0.45f, 0.95f);

        // Inner background
        GameObject innerGO = new GameObject("InnerBg");
        innerGO.transform.SetParent(panelGO.transform, false);
        panelBg = innerGO.AddComponent<Image>();
        panelBg.color = new Color(0.04f, 0.06f, 0.10f, 0.96f);
        RectTransform inr = panelBg.rectTransform;
        inr.anchorMin = Vector2.zero;
        inr.anchorMax = Vector2.one;
        inr.offsetMin = new Vector2(2f, 2f);
        inr.offsetMax = new Vector2(-2f, -2f);

        // Title Text
        GameObject titleGO = new GameObject("TitleText");
        titleGO.transform.SetParent(panelGO.transform, false);
        titleText = titleGO.AddComponent<TextMeshProUGUI>();
        titleText.fontSize = 28f;
        titleText.fontStyle = FontStyles.Bold;
        titleText.alignment = TextAlignmentOptions.Center;
        titleText.color = Color.white;
        RectTransform tr = titleText.rectTransform;
        tr.anchorMin = new Vector2(0f, 0.48f);
        tr.anchorMax = new Vector2(1f, 0.95f);
        tr.offsetMin = new Vector2(16f, 0f);
        tr.offsetMax = new Vector2(-16f, 0f);

        // Subtitle Text
        GameObject subGO = new GameObject("SubText");
        subGO.transform.SetParent(panelGO.transform, false);
        subText = subGO.AddComponent<TextMeshProUGUI>();
        subText.fontSize = 20f;
        subText.fontStyle = FontStyles.Normal;
        subText.alignment = TextAlignmentOptions.Center;
        subText.color = new Color(0.90f, 0.92f, 0.95f, 0.95f);
        RectTransform sr = subText.rectTransform;
        sr.anchorMin = new Vector2(0f, 0.08f);
        sr.anchorMax = new Vector2(1f, 0.52f);
        sr.offsetMin = new Vector2(16f, 0f);
        sr.offsetMax = new Vector2(-16f, 0f);

        panelGO.SetActive(false);
    }

    public static void ShowSuccess(string title = "CORRECT", string subtitle = "Evidence verified. Access granted.", float seconds = 2.4f)
    {
        if (instance == null) Bootstrap();
        if (instance == null) return;
        instance.DisplayInternal(title, subtitle, true, seconds);
    }

    public static void ShowError(string title = "INCORRECT", string subtitle = "Review the evidence and try again.", float seconds = 2.6f)
    {
        if (instance == null) Bootstrap();
        if (instance == null) return;
        instance.DisplayInternal(title, subtitle, false, seconds);
    }

    public static void Show(string message, bool success, float seconds = 2.2f)
    {
        if (instance == null) Bootstrap();
        if (instance == null) return;

        string[] parts = message.Split(new[] { '\n' }, 2);
        string title = parts[0];
        string sub = parts.Length > 1 ? parts[1] : (success ? "Evidence verified." : "Review evidence and try again.");
        title = title.Replace("✓", "").Replace("✕", "").Trim();

        instance.DisplayInternal(title, sub, success, seconds);
    }

    private void DisplayInternal(string title, string subtitle, bool success, float seconds)
    {
        if (panelBg == null || titleText == null) BuildUI();

        titleText.text = title;
        subText.text = subtitle;

        Color highlight = success ? new Color(0.18f, 0.88f, 0.45f) : new Color(0.92f, 0.22f, 0.20f);
        titleText.color = highlight;
        if (panelBorder != null) panelBorder.color = highlight;

        if (routine != null) StopCoroutine(routine);
        routine = StartCoroutine(AnimatePopup(seconds));
    }

    private IEnumerator AnimatePopup(float duration)
    {
        panelRect.gameObject.SetActive(true);
        canvasGroup.alpha = 0f;
        panelRect.localScale = Vector3.one * 0.88f;

        // Pop in animation
        float elapsed = 0f;
        while (elapsed < 0.22f)
        {
            elapsed += Time.unscaledDeltaTime;
            float t = Mathf.Clamp01(elapsed / 0.22f);
            float smooth = Mathf.SmoothStep(0f, 1f, t);
            canvasGroup.alpha = smooth;
            panelRect.localScale = Vector3.Lerp(Vector3.one * 0.88f, Vector3.one, smooth);
            yield return null;
        }

        canvasGroup.alpha = 1f;
        panelRect.localScale = Vector3.one;

        // Display hold
        yield return new WaitForSecondsRealtime(duration);

        // Fade out animation
        elapsed = 0f;
        while (elapsed < 0.25f)
        {
            elapsed += Time.unscaledDeltaTime;
            float t = Mathf.Clamp01(elapsed / 0.25f);
            canvasGroup.alpha = 1f - t;
            yield return null;
        }

        panelRect.gameObject.SetActive(false);
        routine = null;
    }
}
