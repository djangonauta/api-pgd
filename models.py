"""Definições dos modelos de dados da API que serão persistidos no
banco pelo ORM do SQLAlchemy.
"""

from sqlalchemy import (Boolean, Column, ForeignKey,
                        Integer, String, Float, Date, UniqueConstraint)
from sqlalchemy.orm import relationship

from database import Base

class PlanoTrabalho(Base):
    "Plano de Trabalho"
    __tablename__ = 'plano_trabalho'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cod_unidade = Column(Integer)
    cod_plano = Column(String)
    matricula_siape = Column(Integer)
    cpf = Column(String)
    nome_participante = Column(String)
    cod_unidade_exercicio = Column(Integer)
    nome_unidade_exercicio = Column(String)
    local_execucao = Column(Integer)
    carga_horaria_semanal = Column(Integer)
    data_inicio = Column(Date)
    data_fim = Column(Date)
    carga_horaria_total = Column(Float)
    data_interrupcao = Column(Date)
    entregue_no_prazo = Column(Boolean) #TODO Na especificação está como Int e usa 1 e 2 para sim e não. Não seria melhor usar bool?
    horas_homologadas = Column(Float)
    atividades = relationship('Atividade', back_populates='plano_trabalho')
    __table_args__ = (UniqueConstraint(
        'cod_unidade',
        'cod_plano',
        name='_unidade_plano_uc'
    ),)

class Atividade(Base):
    "Atividade"
    __tablename__ = 'atividade'
    id_atividade = Column(Integer, primary_key=True, index=True)
    cod_unidade = Column(Integer)
    # id_plano_trabalho = Column(Integer, ForeignKey('plano_trabalho.id'))
    id_plano_trabalho = Column('id_plano_trabalho', Integer(), ForeignKey('plano_trabalho.id'), nullable=False)
    nome_grupo_atividade = Column(String)
    nome_atividade = Column(String)
    faixa_complexidade = Column(String)
    parametros_complexidade = Column(String)
    tempo_exec_presencial = Column(Float)
    tempo_exec_teletrabalho = Column(Float)
    entrega_esperada = Column(String)
    qtde_entregas = Column(Integer)
    qtde_entregas_efetivas = Column(Integer)
    avaliacao = Column(Integer)
    data_avaliacao = Column(Date)
    justificativa = Column(String)
    plano_trabalho = relationship('PlanoTrabalho', back_populates='atividades')
    __table_args__ = (UniqueConstraint(
        'cod_unidade',
        'id_atividade',
        name='_unidade_atividade_uc'
    ),)
