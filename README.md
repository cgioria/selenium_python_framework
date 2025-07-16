# 🚀 Selenium Python Automation Framework (BDD + POM)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Selenium](https://img.shields.io/badge/Selenium-4.0%2B-green?logo=selenium)
![Behave](https://img.shields.io/badge/Behave-BDD-orange)
![POM](https://img.shields.io/badge/Pattern-Page_Object_Model-blueviolet)

Framework de automatización web con:
- **Selenium WebDriver** para interacción con navegadores
- **Behave** para enfoque BDD (Behavior-Driven Development)
- **Page Object Model** para diseño mantenible


## 🔧 Instalación

1. Clonar repositorio:
```bash
git clone https://github.com/tu-usuario/selenium-python-framework.git
cd selenium-python-framework

pip install -r requirements.txt

## 🔧 Características

- ✅ Compatible con Selenium 4+
- ✅ Soporte para BDD con Gherkin
- ✅ Diseño con Page Object Model
- ✅ Generación de reportes HTML/Allure
- ✅ Integración con CI/CD
- ✅ Configuración multi-navegador

Para personalizar el framework, modifique los archivos de configuración en `utilities/config_manager.py`.


## 🔧 Ejecucion

pytest tests/test_selenium.py

pytest tests/test_login.py --html=reports/detailed_report.html --self-contained-html -v


