import QtQuick
import QtQuick3D
import QtQuick.Layouts
import QtQuick.Controls
import QtQuick3D.Helpers

Item {
    id: root
    //! id: window
    width: 640
    height: 480
    //! visible: true
    property alias cameraPositionZ: camera.position.z


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
            id: model_cy
            position: Qt.vector3d(0, 100, 0)
            source: "#Cylinder"
            scale: Qt.vector3d(1, 1, 1)
            materials: [ DefaultMaterial { diffuseColor: "red" }]
            opacity: 1.0
        }

        Model {
            id: model_cu_1
            position: Qt.vector3d(0, -100, 0)
            source: "#Cube"
            materials: [ DefaultMaterial { diffuseColor: "blue" }]
            opacity: 1.0
        }
        Model {
            id: model_cu_2
            position: Qt.vector3d(-100, -0, 0)
            source: "#Cube"
            scale: Qt.vector3d(2, 1, 1)
            materials: [ DefaultMaterial { diffuseColor: "green" }]
            opacity: 1.0
        }
        Model {
            id: model_cu_3
            position: Qt.vector3d(120, -50, 0)
            source: "#Cube"
            materials: [ DefaultMaterial { diffuseColor: "green" }]
            opacity: 1.0
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
                    let dx = (mouse.x - lastPos.x) / 20
                    let dy = (mouse.y - lastPos.y) / 20
                    console.log("Right Button - dx:", dx, "dy:", dy); // Add for debugging
                    camera.position.x -= dx
                    camera.position.y += dy
                    lastPos = mouse
                }
                else if (mouseArea.pressedButtons & Qt.LeftButton) {
                    let dx = mouse.x - lastPos.x
                    let dy = mouse.y - lastPos.y
                    console.log("Left Button - dx:", dx, "dy:", dy); // Add for debugging
                    camera.eulerRotation.y -= dx / 20
                    camera.eulerRotation.x -= dy / 20
                    lastPos = mouse
                }
            }
        }

    }
    WasdController {
        controlledObject: camera
    }

    Button {
        id: button_1on
        text: qsTr("p_1 x")
        x: 5
        y: 5
        onClicked: model_cu_1.opacity= 0;
    }
    Button {
        id: button_1off
        text: qsTr("√")
        x: 40
        y: 5
        onClicked: model_cu_1.opacity= 1;
    }

     Button {
        id: button_2on
        text: qsTr("p_2 x")
        x: 5
        y: 30
        onClicked: model_cu_2.opacity= 0;
    }
    Button {
        id: button_2off
        text: qsTr("√")
        x: 40
        y: 30
        onClicked: model_cu_2.opacity= 1;
    }

     Button {
        id: button_3on
        text: qsTr("p_3 x")
        x: 5
        y: 55
        onClicked: model_cu_3.opacity= 0;
    }
    Button {
        id: button_3off
        text: qsTr("√")
        x: 40
        y: 55
        onClicked: model_cu_3.opacity= 1;
    }

    Button {
        id: button_4on
        text: qsTr("p_4 x")
        x: 5
        y: 80
        onClicked: model_cy.opacity= 0;
    }
    Button {
        id: button_4off
        text: qsTr("√")
        x: 40
        y: 80
        onClicked: model_cy.opacity= 1;
    }

    Connections {
        target: main_app  // MainApp instance set in Python

        onZoomChanged: {
            // Adjust the camera's position based on the zoom value
            camera.position.z = zoomValue // zoomValue should be calculated in Python
        }

        onTransparencyChanged: {
            // Adjust the model's opacity
            model_cy.opacity = transparencyValue // transparencyValue should be a float between 0 and 1, calculated in Python
        }

        onMaterialChanged: {
            let isMaterialChanged = changeMaterial; // Boolean indicating if material should be changed
            let modelId = model_id; // The ID of the model to change

            // Define original colors for each model
            let originalColors = {
                "model_cy": "red",
                "model_cu_1": "blue",
                "model_cu_2": "green",
                "model_cu_3": "green"
            };

            let newColor = isMaterialChanged ? "some_other_color" : originalColors[modelId];

            switch (modelId) {
                case "model_cy":
                    model_cy.materials[0].diffuseColor = "yellow";
                    break;
                case "model_cu_1":
                    model_cu_1.materials[0].diffuseColor = "yellow";
                    break;
                case "model_cu_2":
                    model_cu_2.materials[0].diffuseColor = "yellow";
                    break;
                case "model_cu_3":
                    model_cu_3.materials[0].diffuseColor = "yellow";
                    break;
            }
        }
    }
}
