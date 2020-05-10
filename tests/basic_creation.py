import mongoengine as me
from rango.schemas import job, site, stem
import datetime

me.connect(db='jinx', host='localhost', port=18732)

tj = job.Job()
tj.label = 'GARB'
tj.created = datetime.datetime.today()
tj.modified = tj.created
tj.job = 'GARB'
tj.state = True
tj.path = '/jobs/GARB'
tj.generate_id()
tj.resolution = [2560, 1440]
tj.description = """This is a show about garbage truck.
There is several trucks,
and environment,
and a human character.
"""
tj.tags = ['truck', 'environment', 'sci-fi']
# tj.save()

ts = stem.Stem()
ts.label = 'aa_seq'
ts.created = datetime.datetime.today()
ts.modified = ts.created
ts.job = 'GARB'
ts.directory = 'GARB/aa_seq'
ts.path = '/jobs/GARB/aa_seq'
ts.type = 'sequence'
ts.production = True
ts.generate_id()
# ts.save()

obj = job.Job.objects()[0]
print(obj.sequences())

me.disconnect()
