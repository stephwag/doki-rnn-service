FROM python:3.6.6

COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
COPY weights/renpy_script_ddlc.hdf5 /renpy_script_ddlc.hdf5
COPY main.py /
CMD [ "python", "/main.py" ]