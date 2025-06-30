# Usar la imagen base oficial AWS Lambda Python 3.12
FROM public.ecr.aws/lambda/python:3.12-x86_64

# Copiar requirements y código fuente al directorio Lambda
COPY requirements.txt ${LAMBDA_TASK_ROOT}/
RUN pip install -r ${LAMBDA_TASK_ROOT}/requirements.txt

# Copiar todo el código fuente (ajusta según tu estructura)
COPY functions/ ${LAMBDA_TASK_ROOT}/functions/
COPY core.py ${LAMBDA_TASK_ROOT}/
COPY config.py ${LAMBDA_TASK_ROOT}/
COPY lambda_function.py ${LAMBDA_TASK_ROOT}/

# Establecer el handler Lambda (archivo.función)
CMD ["lambda_function.lambda_handler"]
