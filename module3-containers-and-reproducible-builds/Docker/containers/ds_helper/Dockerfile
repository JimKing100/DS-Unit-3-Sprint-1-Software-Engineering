FROM debian

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get upgrade -y && \
apt-get install python3-pip curl nano -y && \

pip3 install pandas numpy  && \
pip3 install -i https://test.pypi.org/simple/ ds_helper && \
python3 -c "from ds_helper_data import df_utils; print; print('Success') "
