# Segmentacion_inteligente_abogados
Desarrollar un modelo de segmentación para agrupar abogados de acuerdo con la demanda de trabajo, con el propósito de identificar perfiles de oferta y servicio, que fortalezcan la especialización profesional, permitiendo optimizar la asignación de casos, priorizar planes de capacitación y optimización del presupuesto de demandas.

[CONTEXTO]

Las entidades del sector financiero (bancos, aseguradoras, cooperativas y fondos de pensiones) manejan un alto volumen de procesos jurídicos relacionados con sus empleados: demandas laborales, procesos disciplinarios, conciliaciones, litigios contractuales y casos especiales derivados de la regulación estricta del sector.
Estos procesos deben ser gestionados por equipos jurídicos internos o externos, que presentan perfiles diversos en experiencia y especialidad (laboral, disciplinario, administrativo, civil).Sin embargo, el crecimiento del sector, la rotación de personal y la complejidad normativa hacen cada vez más difícil asignar de manera eficiente los casos a los abogados más idóneos, manteniendo la calidad del servicio jurídico, reduciendo costos y protegiendo la reputación institucional.

En este contexto, la analítica avanzada y el Machine Learning se perfilan como herramientas estratégicas para apoyar la toma de decisiones sobre asignación de casos, capacitación y optimización de recursos jurídicos, contribuyendo a mejorar la gestión legal interna del sector financiero

[PROBLEMATICA]

<img width="1203" height="576" alt="image" src="https://github.com/user-attachments/assets/a0b6dafa-b977-4a60-bb57-7599edb5e9ce" />

[OBJETIVO GENERAL]


Desarrollar un modelo de segmentación basado en k-means para agrupar abogados de acuerdo con la demanda de trabajo (ordinario, ejecutivo, único y especial), con el propósito de identificar perfiles de oferta y servicio que faciliten los casos de éxito y fortalezcan la especialización profesional, permitiendo optimizar la asignación de casos, priorizar planes de capacitación y optimización del presupuesto de demandas.

[OBJETIVOS ESPECIFICOS]

1. Recolectar y organizar la información relevante sobre abogados y demandas de trabajo (ordinario, ejecutivo, único y especial), consolidando variables que reflejen su desempeño, experiencia y nivel de especialización.
2. Preprocesar y transformar los datos mediante técnicas de limpieza, codificación y normalización, garantizando su calidad y pertinencia para la aplicación del modelo de segmentación.
3. Definir y preparar las variables relevantes para el análisis no supervisado, asegurando la calidad, consistencia y anonimización de los datos sensibles.
4. Realizar análisis descriptivo con las variables que finalmente seleccionemos en el modelo, para encontrar hallazgosy patrones que generen valor en la toma de decisiones. 
5. Implementar un modelo de segmentación con K-Means para agrupar abogados en clústeres según su perfil y desempeño frente a los distintos tipos de procesos jurídicos laborales.
6. Evaluar y validar los resultados de la segmentación, identificando patrones y características comunes en cada grupo que permitan generar perfiles de oferta y servicio jurídico interno.

Recomendaciones estratégicas:

1. Diseñar lineamientos para la asignación estratégica de casos a partir de los clústeres obtenidos, priorizando la optimización de recursos, la especialización y la reducción de tiempos de respuesta.
2. Proponer planes de formación y capacitación para fortalecer las competencias de los abogados según las necesidades detectadas en cada clúster.
3. Elaborar recomendaciones para la optimización del presupuesto destinado a la gestión jurídica interna en función de los hallazgos del modelo.


[PREGUNTAS DE NEGOCIO]

<img width="1499" height="838" alt="image" src="https://github.com/user-attachments/assets/4bca2c67-a24c-4007-87ff-ab8a4e9643e4" />


[MÉTRICAS]

Métricas estratégicas:
Tasa de éxito de acuerdo a la segmentación del modelo


Métrica técnica:
Reducir Within-Cluster Sum of Squares 
Optimiza Silhouette Score









