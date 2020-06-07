FROM centos

RUN yum install wget -y 
RUN yum install sudo -y 
RUN yum install python2 -y
RUN yum install python36 -y
RUN yum install epel-release  -y 
RUN sudo yum update -y 

RUN curl "https://bootstrap.pypa.io/get-pip.py"  -o  "get-pip.py"
RUN python3 get-pip.py
RUN pip install setuptools

RUN mkdir  tensorflow_project
RUN cd tensorflow_project
RUN python3 -m venv venv
RUN source venv/bin/activate
RUN pip3 install --upgrade pip
RUN pip3 install  tensorflow==2.0
RUN pip3 install numpy
RUN pip3 install keras

COPY cnn_model.py / 
COPY  cnn-cat-dog-dataset /
RUN pip3 install pillow

CMD ["python3" , "cnn_model.py"] > result.txt

COPY mail.py /


