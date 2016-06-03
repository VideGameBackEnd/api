from rest_framework.authentication import BasicAuthentication
 
"""
Quite basic authentication
"""
class QuietBasicAuthentication(BasicAuthentication) :
    def authenticate_header(self, request):
        return ( 'xBasic realm="{0}"' ).format( self.www_authenticate_realm )
#End of quite basic authentication class