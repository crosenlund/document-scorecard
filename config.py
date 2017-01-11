import os

basedir = os.path.abspath(os.path.dirname(__file__))

# configuration file for the app. This is where the upload folder and database are set globally.


# -------------------------------------------------------------------------------
# This is for the use on the ubuntu server

APP_FOLDER = 'app'
UPLOAD_FOLDER = APP_FOLDER + '/ALL_UPLOADS'
SCHEMA_FOLDER = APP_FOLDER + '/SCHEMAS'
SCHEMA_LAYOUTS_FOLDER = APP_FOLDER + '/SCHEMA_LAYOUTS'
GENERATEDS_FOLDER = 'generateDS'
BASE_FOLDER = basedir
# SQLALCHEMY_DATABASE_URI = 'postgresql:///scorecard'
# SQLALCHEMY_BINDS = {'usagedb': 'postgresql:///appusage',}
# APP_NAME = 'DSC'
# -------------------------------------------------------------------------------

SECRET_KEY = '0Zr98j/3yX R~XHH!jmN]LWX/,?RTA'
