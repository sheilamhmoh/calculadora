pipeline {
    agent any  // Ejecutar en cualquier agente disponible

    environment {
        PYTHON = 'python3'  // Asegúrate de tener python3 instalado en tu entorno
    }

    stages {
        stage('Install dependencies') {
            steps {
                script {
                    // Instalar dependencias (si tienes algún requerimiento como pytest o unittest)
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Run tests') {
            steps {
                script {
                    // Ejecutar las pruebas
                    sh 'python3 -m unittest discover'
                }
            }
        }
    }

    post {
        always {
            // Este bloque se ejecuta independientemente del estado del build
            echo 'Fin de la ejecución de la canalización'
        }

        success {
            echo 'La canalización se completó correctamente'
        }

        failure {
            echo 'La canalización falló'
        }
    }
}
