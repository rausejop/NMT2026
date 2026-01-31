"""
Script para generar todos los archivos markdown del temario NMT 2026
"""

import os
import sys
from pathlib import Path

# Configurar encoding para Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Ruta base
BASE_PATH = r"c:\_CONFIANZA23\PERSONAL\PERSONAS 00 LUDA\01 Estudios NMT 2026"

# Datos de Lengua Ucraniana
lengua_ucraniana = [
    {"num": "01", "titulo": "Introducción - Presentación y Características de la Prueba", "url": "https://www.youtube.com/watch?v=JMYW6GMSsUg"},
    {"num": "02", "titulo": "Fonética, Gráficos y Ortoepía", "url": "https://www.youtube.com/live/zzaAUQJuDm8"},
    {"num": "03", "titulo": "Ortografía - Parte 1", "url": "https://www.youtube.com/live/5HflyPoYrGo"},
    {"num": "04", "titulo": "Ortografía - Parte 2", "url": "https://www.youtube.com/live/Y1BFdH_3RIU"},
    {"num": "05", "titulo": "Ortografía - Parte 3", "url": "https://www.youtube.com/live/RkxFqkNK5n0"},
    {"num": "06", "titulo": "Lexicología", "url": "https://www.youtube.com/live/M9yFIiZe7W0"},
    {"num": "07", "titulo": "Fraseología", "url": "https://www.youtube.com/watch?v=8o3QHg6UhSM"},
    {"num": "08", "titulo": "Estructura de Palabras - Formación de Palabras", "url": "https://www.youtube.com/watch?v=5EmCyc1EDJY"},
    {"num": "09", "titulo": "Sustantivo - Parte 1", "url": "https://www.youtube.com/watch?v=ih7oKazdFPA"},
    {"num": "10", "titulo": "Sustantivo - Parte 2", "url": "https://www.youtube.com/watch?v=PpfjDBL4f-s"},
    {"num": "11", "titulo": "Adjetivo y Numeral", "url": "https://www.youtube.com/watch?v=9hs3Ml5A4fo"},
    {"num": "12", "titulo": "Pronombre, Verbo y Adverbio", "url": "https://www.youtube.com/watch?v=Gm69SaNcz9A"},
    {"num": "13", "titulo": "Participio y Gerundio", "url": "https://www.youtube.com/watch?v=JwjqubE_9DI"},
    {"num": "14", "titulo": "Partes de Servicio e Interjección", "url": "https://www.youtube.com/watch?v=Eery7gxVK7Q"},
    {"num": "15", "titulo": "Frases y Oraciones - Sujeto y Predicado", "url": "https://www.youtube.com/watch?v=qmkikhHPkZs"},
    {"num": "16", "titulo": "Complementos y Giro Comparativo", "url": "https://www.youtube.com/watch?v=qmGfvIc0Q9U"},
    {"num": "17", "titulo": "Oraciones Monosilábicas", "url": "https://www.youtube.com/watch?v=1KtmR2fipG0"},
    {"num": "18", "titulo": "Oración Simple y Compleja - Parte 1", "url": "https://www.youtube.com/watch?v=nFvSs8CtkBk"},
    {"num": "19", "titulo": "Oración Simple y Compleja - Parte 2", "url": "https://www.youtube.com/watch?v=yqrNxA9_nsk"},
    {"num": "20", "titulo": "Elementos Separados de la Oración", "url": "https://www.youtube.com/watch?v=_ozyoomjhkc"},
    {"num": "21", "titulo": "Tipos de Oraciones Complejas - Parte 1", "url": "https://www.youtube.com/watch?v=efmSgoOa3CQ"},
    {"num": "22", "titulo": "Tipos de Oraciones Complejas - Parte 2", "url": "https://www.youtube.com/watch?v=BUXMppthwRA"},
    {"num": "23", "titulo": "Oración Compleja sin Conjunción", "url": "https://www.youtube.com/watch?v=3BaWClgqMWM"},
    {"num": "24", "titulo": "Reproducción del Habla Ajena y Estilística", "url": "https://www.youtube.com/watch?v=SQCN6HVpp1c"},
    {"num": "25", "titulo": "Modelado NMT - Lección Final", "url": "https://www.youtube.com/watch?v=1oP_nFvEmrI"},
]

# Datos de Historia de Ucrania
historia_ucrania = [
    {"num": "01", "titulo": "Introducción - Historia Antigua de Ucrania", "url": "https://www.youtube.com/live/eyAhiGNtqII"},
    {"num": "02", "titulo": "Rus-Ucrania (Estado de Kiev)", "url": "https://www.youtube.com/live/1JYDceiOEfQ"},
    {"num": "03", "titulo": "Reino de Rus (Galicia-Volinia) - Invasión Mongola", "url": "https://www.youtube.com/live/zGVfLJlbfTw"},
    {"num": "04", "titulo": "Principados de Rus en Estados Extranjeros", "url": "https://www.youtube.com/live/RPED5uZP8Ac"},
    {"num": "05", "titulo": "Territorios Ucranianos en la Mancomunidad Polaco-Lituana (s. XVI-XVII)", "url": "https://www.youtube.com/live/J4PiVWjButE"},
    {"num": "06", "titulo": "Guerra de Liberación Nacional (s. XVII)", "url": "https://www.youtube.com/live/PsuS7vS1wkI"},
    {"num": "07", "titulo": "Ucrania Cosaca (finales s. XVII)", "url": "https://www.youtube.com/live/ziyqKLLg12Y"},
    {"num": "08", "titulo": "Territorios Ucranianos (finales s. XVII - s. XVIII)", "url": "https://www.youtube.com/live/lzn4yX7wY8M"},
    {"num": "09", "titulo": "Territorios en el Imperio Ruso (s. XVIII-XIX)", "url": "https://www.youtube.com/live/YltDD58EYlQ"},
    {"num": "10", "titulo": "Territorios en el Imperio Austríaco (s. XVIII-XIX)", "url": "https://www.youtube.com/live/_pXsnal5W0s"},
    {"num": "11", "titulo": "Territorios en el Imperio Ruso (s. XIX)", "url": "https://www.youtube.com/live/j7f9mIfArXw"},
    {"num": "12", "titulo": "Territorios en Austria-Hungría (s. XIX)", "url": "https://www.youtube.com/live/8sdVeWp4J7I"},
    {"num": "13", "titulo": "Repetición", "url": "https://www.youtube.com/live/mr-hkkvuQNQ"},
    {"num": "14", "titulo": "Territorios Ucranianos 1900-1914", "url": "https://www.youtube.com/live/rk5N3EQi5Ms"},
    {"num": "15", "titulo": "Ucrania en la Primera Guerra Mundial", "url": "https://www.youtube.com/live/94a1gNfkSNc"},
    {"num": "16", "titulo": "Desarrollo de la Revolución Ucraniana", "url": "https://www.youtube.com/live/zkJkngfiINM"},
    {"num": "17", "titulo": "Establecimiento del Régimen Totalitario Comunista", "url": "https://www.youtube.com/live/l8qtJr6wSmo"},
    {"num": "18", "titulo": "Establecimiento del Régimen Totalitario Bolchevique", "url": "https://www.youtube.com/live/5y6Ic8V7_4Q"},
    {"num": "19", "titulo": "Territorios de Ucrania Occidental (Período de Entreguerras)", "url": "https://www.youtube.com/live/EuRRQIVeJ1U"},
    {"num": "20", "titulo": "Ucrania en la Segunda Guerra Mundial", "url": "https://www.youtube.com/live/BFJnsppoCt8"},
    {"num": "21", "titulo": "Ucrania en la Posguerra y Desestalinización", "url": "https://www.youtube.com/live/f4qt5CTTeyg"},
    {"num": "22", "titulo": "Crisis del Sistema Soviético e Independencia", "url": "https://www.youtube.com/live/tFtYhzzNZtg"},
    {"num": "23", "titulo": "Formación de Ucrania como Estado Independiente", "url": "https://www.youtube.com/live/VoSANS1lU3M"},
    {"num": "24", "titulo": "Repetición - Pruebas sobre el Siglo XX", "url": "https://www.youtube.com/live/7n4auoCKpZU"},
]

# Datos de Biología
biologia = [
    {"num": "01", "titulo": "Composición Química de la Célula", "url": "https://www.youtube.com/watch?v=iwgmJjEO9g0"},
    {"num": "02", "titulo": "Estructura y Funcionamiento de Células Eucariotas", "url": "https://www.youtube.com/watch?v=o40iVQflTTw"},
    {"num": "03", "titulo": "Preservación e Implementación de Información Hereditaria", "url": "https://www.youtube.com/watch?v=Xygtw8bQllI"},
    {"num": "04", "titulo": "Patrones de Herencia y Variabilidad", "url": "https://www.youtube.com/watch?v=KLkQGfTzsfE"},
    {"num": "05", "titulo": "Biodiversidad - Virus y Procariotas", "url": "https://www.youtube.com/watch?v=TI2LhOeX3Ms"},
    {"num": "06", "titulo": "Biodiversidad - Plantas y Hongos", "url": "https://www.youtube.com/watch?v=lhKZNhWo6XA"},
    {"num": "07", "titulo": "Biodiversidad - Animales", "url": "https://www.youtube.com/watch?v=w7oF2ikoLrU"},
    {"num": "08", "titulo": "Biología Humana - Sistemas Reguladores", "url": "https://www.youtube.com/watch?v=Jm11CRb7juk"},
    {"num": "09", "titulo": "Biología Humana - Sistemas Viscerales Parte 1", "url": "https://www.youtube.com/watch?v=-ZYZwEP9TLM"},
    {"num": "10", "titulo": "Biología Humana - Sistemas Viscerales Parte 2", "url": "https://www.youtube.com/watch?v=JIe0qAlfKQI"},
]

def generar_contenido_lengua(unidad):
    return f"""# U{unidad['num']}: {unidad['titulo']}

## 📹 Video de la Lección

**Enlace:** [{unidad['titulo']}]({unidad['url']})

## 📚 Contenido de la Unidad

### Objetivos de Aprendizaje

Al completar esta unidad, deberás ser capaz de:

- ✅ Comprender los conceptos fundamentales de {unidad['titulo'].lower()}
- ✅ Aplicar las reglas y principios en ejercicios prácticos
- ✅ Identificar errores comunes y corregirlos
- ✅ Resolver preguntas tipo NMT sobre este tema

### Conceptos Clave

> [!IMPORTANT]
> Esta sección cubre material esencial para el examen NMT 2026.

### Contenido Detallado

_Contenido basado en el video de la lección y material complementario_

### Ejemplos Prácticos

### Ejercicios de Práctica

### Errores Comunes

> [!WARNING]
> Presta atención a estos errores frecuentes.

## 📝 Resumen

## 🔗 Recursos Adicionales

- Video de la lección: {unidad['url']}
- Material oficial NMT: [testportal.gov.ua](https://testportal.gov.ua)

## ✅ Autoevaluación

- [ ] He visto el video completo
- [ ] He tomado notas
- [ ] He completado los ejercicios
- [ ] Puedo explicar los conceptos clave

---

**Última actualización:** Enero 2026
"""

def generar_contenido_historia(unidad):
    return f"""# U{unidad['num']}: {unidad['titulo']}

## 📹 Video de la Lección

**Enlace:** [{unidad['titulo']}]({unidad['url']})

## 📚 Contenido de la Unidad

### Contexto Histórico

### Eventos Principales

### Personajes Clave

### Cronología

```mermaid
timeline
    title Eventos Principales
    section Período
        Evento 1
        Evento 2
        Evento 3
```

### Mapa Conceptual

```mermaid
graph TD
    A[{unidad['titulo']}] --> B[Contexto Político]
    A --> C[Contexto Social]
    A --> D[Contexto Cultural]
    A --> E[Consecuencias]
```

### Análisis Detallado

### Fuentes Históricas

### Importancia Histórica

## 📝 Resumen

## 🔗 Recursos Adicionales

- Video de la lección: {unidad['url']}
- Material oficial NMT: [testportal.gov.ua](https://testportal.gov.ua)

## ✅ Autoevaluación

- [ ] He visto el video completo
- [ ] Comprendo el contexto histórico
- [ ] Puedo explicar los eventos principales
- [ ] Conozco los personajes clave
- [ ] Puedo situar los eventos en la cronología

---

**Última actualización:** Enero 2026
"""

def generar_contenido_biologia(unidad):
    return f"""# U{unidad['num']}: {unidad['titulo']}

## 📹 Video de la Lección

**Enlace:** [{unidad['titulo']}]({unidad['url']})

## 📚 Contenido de la Unidad

### Objetivos de Aprendizaje

Al completar esta unidad, deberás ser capaz de:

- ✅ Comprender los conceptos biológicos fundamentales
- ✅ Identificar estructuras y procesos celulares
- ✅ Explicar mecanismos biológicos
- ✅ Resolver problemas y preguntas tipo NMT

### Conceptos Fundamentales

> [!IMPORTANT]
> Esta sección cubre material esencial para el examen NMT 2026.

### Diagrama de Procesos

```mermaid
graph LR
    A[Inicio] --> B[Proceso 1]
    B --> C[Proceso 2]
    C --> D[Resultado]
```

### Contenido Detallado

### Estructuras Biológicas

### Procesos y Mecanismos

### Aplicaciones Prácticas

### Experimentos y Observaciones

## 📝 Resumen

## 🔗 Recursos Adicionales

- Video de la lección: {unidad['url']}
- Material oficial NMT: [testportal.gov.ua](https://testportal.gov.ua)

## ✅ Autoevaluación

- [ ] He visto el video completo
- [ ] Comprendo los conceptos fundamentales
- [ ] Puedo explicar los procesos biológicos
- [ ] He revisado los diagramas
- [ ] Puedo resolver ejercicios prácticos

---

**Última actualización:** Enero 2026
"""

def generar_matematica():
    return """# U01: Repaso General y Ensayo General

## 📹 Video de la Lección

**Enlace:** [НМТ 2025. Matemática. Seminario 25. Resultados. Ensayo General](https://www.youtube.com/live/iRvvFVIJUjI)

## 📚 Contenido de la Unidad

### Estructura del Examen de Matemática NMT 2026

El examen de matemática del NMT 2026 evalúa competencias en:

- Álgebra
- Geometría
- Trigonometría
- Análisis matemático
- Probabilidad y estadística

### Temas Principales

#### 1. Álgebra
- Ecuaciones y sistemas de ecuaciones
- Desigualdades
- Funciones
- Progresiones
- Logaritmos y exponenciales

#### 2. Geometría
- Geometría plana
- Geometría del espacio
- Trigonometría
- Coordenadas y vectores

#### 3. Análisis
- Límites
- Derivadas
- Integrales
- Aplicaciones

#### 4. Probabilidad y Estadística
- Combinatoria
- Probabilidad
- Estadística descriptiva

### Estrategias de Resolución

```mermaid
graph TD
    A[Leer el Problema] --> B[Identificar Datos]
    B --> C[Determinar Método]
    C --> D[Resolver]
    D --> E[Verificar]
```

### Fórmulas Esenciales

> [!IMPORTANT]
> Memoriza estas fórmulas clave para el examen.

#### Álgebra
- Fórmula cuadrática: $x = \\frac{-b \\pm \\sqrt{b^2-4ac}}{2a}$
- Suma de progresión aritmética: $S_n = \\frac{n(a_1+a_n)}{2}$

#### Geometría
- Área del círculo: $A = \\pi r^2$
- Volumen de la esfera: $V = \\frac{4}{3}\\pi r^3$

#### Trigonometría
- Identidad fundamental: $\\sin^2\\theta + \\cos^2\\theta = 1$

### Ejercicios de Práctica

### Errores Comunes

> [!WARNING]
> Evita estos errores frecuentes:
> - No verificar las soluciones
> - Errores de signo
> - Confundir fórmulas similares
> - No leer cuidadosamente el enunciado

## 📝 Resumen

## 🔗 Recursos Adicionales

- Video de la lección: https://www.youtube.com/live/iRvvFVIJUjI
- Material oficial NMT: [testportal.gov.ua](https://testportal.gov.ua)

## ✅ Autoevaluación

- [ ] He visto el video completo
- [ ] Conozco las fórmulas esenciales
- [ ] Puedo resolver problemas de cada tema
- [ ] He practicado con cronómetro
- [ ] Comprendo las estrategias de resolución

---

**Última actualización:** Enero 2026
"""

# Generar archivos
def generar_archivos():
    # Lengua Ucraniana
    dir_lengua = Path(BASE_PATH) / "01 Lengua Ucraniana"
    for unidad in lengua_ucraniana:
        filename = f"U{unidad['num']} {unidad['titulo']}.md"
        filepath = dir_lengua / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(generar_contenido_lengua(unidad))
        print(f"[OK] Creado: {filename}")
    
    # Historia de Ucrania
    dir_historia = Path(BASE_PATH) / "03 Historia de Ucrania"
    for unidad in historia_ucrania:
        filename = f"U{unidad['num']} {unidad['titulo']}.md"
        filepath = dir_historia / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(generar_contenido_historia(unidad))
        print(f"[OK] Creado: {filename}")
    
    # Biología
    dir_biologia = Path(BASE_PATH) / "04 Biología"
    # Primero el U00
    filepath_bio_00 = dir_biologia / "U00 Curso Completo NMT-2024.md"
    with open(filepath_bio_00, 'w', encoding='utf-8') as f:
        f.write("""# U00: Curso Completo NMT-2024 - Biología

## 📹 Playlist Completa

**Enlace:** [НМТ-2024. Curso Completo - Biología](https://www.youtube.com/playlist?list=PLH1iFGL1sy5gtx154BU6rDLhmLXVySPvf)

## 📚 Descripción del Curso

Este curso completo cubre todos los temas de biología necesarios para el examen NMT 2024-2026.

### Temas Principales

1. Composición química de la célula
2. Estructura y función celular
3. Genética y herencia
4. Biodiversidad
5. Biología humana
6. Ecología

---

**Última actualización:** Enero 2026
""")
    print("✓ Creado: U00 Curso Completo NMT-2024.md (Biología)")
    
    for unidad in biologia:
        filename = f"U{unidad['num']} {unidad['titulo']}.md"
        filepath = dir_biologia / filename
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(generar_contenido_biologia(unidad))
        print(f"[OK] Creado: {filename}")
    
    # Matemática
    dir_matematica = Path(BASE_PATH) / "02 Matemática"
    filepath_mat = dir_matematica / "U01 Repaso General y Ensayo General.md"
    with open(filepath_mat, 'w', encoding='utf-8') as f:
        f.write(generar_matematica())
    print("✓ Creado: U01 Repaso General y Ensayo General.md (Matemática)")
    
    print("\n✅ Todos los archivos han sido generados exitosamente!")

if __name__ == "__main__":
    generar_archivos()
