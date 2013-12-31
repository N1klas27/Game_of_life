from projectconway.models import Base
from sqlalchemy import Column, DateTime, Index, Integer, Sequence, String


class Run(Base):
    '''
    This class contains the logic necessary for the database to hold
    an instance of the Run table, in which a single run of the
    Game Of Life will be held.
    '''
    __tablename__ = "runs"
    
    id = Column(Integer, Sequence('run_id_seq'), primary_key=True)
    input_pattern = Column(String)
    user_name = Column(String(50))
    
    def __init__(self, input_pattern, user_name):
        '''
        Initialises an object to be input into
        the table.
        '''
        self.input_pattern = input_pattern
        self.user_name = user_name
        
    def __repr__(self):
        '''
        Returns: a representation of the table object.
        '''
        return("Run<%s, %s>" % (self.input_pattern, self.user_name))