"""
owtf.models.url
~~~~~~~~~~~~~~~~~~~

"""
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey

from owtf.db.model_base import Model


class Url(Model):
    __tablename__ = "urls"

    target_id = Column(Integer, ForeignKey("targets.id"))
    url = Column(String, primary_key=True)
    visited = Column(Boolean, default=False)
    scope = Column(Boolean, default=True)

    def to_dict(self):
        udict = dict(self.__dict__)
        udict.pop("_sa_instance_state")
        return udict

    def __repr__(self):
        return "<URL (url='{!s}')>".format(self.url)
