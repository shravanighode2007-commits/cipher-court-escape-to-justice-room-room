using UnityEngine;

public class DoorWallBuilder : MonoBehaviour
{
    [Header("Doorway Size")]
    public float wallWidth = 15f;
    public float wallHeight = 5f;
    public float wallThickness = 0.2f;

    public float doorWidth = 2.5f;
    public float doorHeight = 3f;

    [Header("Wall Position")]
    public float wallZ = 7.5f;

    private void Start()
    {
        BuildDoorWall();
    }

    private void BuildDoorWall()
    {
        float sideWidth = (wallWidth - doorWidth) / 2f;
        float topHeight = wallHeight - doorHeight;

        // LEFT WALL
        GameObject leftWall = GameObject.CreatePrimitive(PrimitiveType.Cube);
        leftWall.name = "BackWallLeft";
        leftWall.transform.position = new Vector3(
            -(doorWidth / 2f + sideWidth / 2f),
            wallHeight / 2f,
            wallZ
        );

        leftWall.transform.localScale = new Vector3(
            sideWidth,
            wallHeight,
            wallThickness
        );

        // RIGHT WALL
        GameObject rightWall = GameObject.CreatePrimitive(PrimitiveType.Cube);
        rightWall.name = "BackWallRight";
        rightWall.transform.position = new Vector3(
            (doorWidth / 2f + sideWidth / 2f),
            wallHeight / 2f,
            wallZ
        );

        rightWall.transform.localScale = new Vector3(
            sideWidth,
            wallHeight,
            wallThickness
        );

        // TOP WALL
        GameObject topWall = GameObject.CreatePrimitive(PrimitiveType.Cube);
        topWall.name = "BackWallTop";

        topWall.transform.position = new Vector3(
            0f,
            doorHeight + topHeight / 2f,
            wallZ
        );

        topWall.transform.localScale = new Vector3(
            doorWidth,
            topHeight,
            wallThickness
        );
    }
}