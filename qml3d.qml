import QtQuick
import QtQuick3D

Window {
    id: window
    width: 1280
    height: 720
    visible: true

    View3D {
        id: view
        anchors.fill: parent

        environment: SceneEnvironment {
            clearColor: "skyblue"
            backgroundMode: SceneEnvironment.Color
        }

        PerspectiveCamera {
            id: camera
            position: Qt.vector3d(0, 200, 300)
            eulerRotation.x: -30
        }

        DirectionalLight {
            eulerRotation.x: -30
            eulerRotation.y: -70
        }

        Model {
            position: Qt.vector3d(0, 100, 0)
            source: "#Cylinder"
            scale: Qt.vector3d(1, 1, 1)
            materials: [ DefaultMaterial { diffuseColor: "red" }]
        }

        Model {
            position: Qt.vector3d(0, -100, 0)
            source: "#Cube"
            materials: [ DefaultMaterial { diffuseColor: "blue" }]
        }
        Model {
            position: Qt.vector3d(-100, -0, 0)
            source: "#Cube"
            scale: Qt.vector3d(2, 1, 1)
            materials: [ DefaultMaterial { diffuseColor: "green" }]
        }
        Model {
            position: Qt.vector3d(120, -50, 0)
            source: "#Cube"
            materials: [ DefaultMaterial { diffuseColor: "green" }]
        }

        MouseArea {
            id: mouseArea
            anchors.fill: parent
            property point lastPos

            onWheel: {
                camera.position.z += wheel.angleDelta.y / 20
            }

            onPressed: {
                lastPos = mouse
            }

            onPositionChanged: {
                if (mouseArea.pressedButtons & Qt.RightButton) {
                    let dx = (mouse.x - lastPos.x) / 5
                    let dy = (mouse.y - lastPos.y) / 5
                    console.log("Right Button - dx:", dx, "dy:", dy); // Add for debugging
                    camera.position.x -= dx
                    camera.position.y += dy
                    lastPos = mouse
                }
                else if (mouseArea.pressedButtons & Qt.LeftButton) {
                    let dx = mouse.x - lastPos.x
                    let dy = mouse.y - lastPos.y
                    console.log("Left Button - dx:", dx, "dy:", dy); // Add for debugging
                    camera.eulerRotation.y -= dx / 5
                    camera.eulerRotation.x -= dy / 5
                    lastPos = mouse
                }
            }
        }
    }
}