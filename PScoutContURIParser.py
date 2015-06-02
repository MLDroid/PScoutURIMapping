import sys
import logging
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('sys.stdout')


class PScoutURIMapping (object):
    
    ##################################################
    #                 Constructor                    #
    ##################################################
    def __init__(self, JsonPath):
        with open(JsonPath, 'rb') as FH:
            #Filename of PScout dict is hard-coded
            #It could be changed if needed
            
            self.PermURIMapping = json.load(FH) 


            
    ##################################################
    #                 Get Routines                   #
    ##################################################
    
    def GetAllPerms (self):
        return list (self.PermURIMapping.keys())



    def GetAllUris (self):
        return list(self.PermURIMapping.values())


    
#    def GetUrisFromPerm (self, Perm):
#        PermAsKey = Perm
#        if PermAsKey not in self.PermURIMapping:
#            logger.error ("Permission %s not found in the PScout Dict",
#                           PermAsKey)
#            return -1
#        else:
#            return self.PermURIMapping[PermAsKey]
#
#
#        
#    def GetPermFromUri (self, CheckUri):
#        for PermAsKey in self.PermURIMapping.keys():
#            Perm = PermAsKey
#            logger.debug ("Checking if the permission associated is %s",
#                          Perm)
#            
#            for MappedUri in self.PermURIMapping[Perm]:
#                # if Api[0].lower() == ApiClass.lower() and \
#                # Api[1].lower() == ApiMethodName.lower():
#                if MappedUri.lower() == CheckUri.lower() :
#                    logger.info("for URI %s PScout maps permission %s", 
#                             CheckUri, Perm)
#                    return Perm
#        #logger.info ("Unable to find any permission\
#        #associated to this API %s %s", ApiClass, ApiMethodName)
#        return None 



def Main ():
    PS = PScoutURIMapping ('PScoutURIs.json')
    print PS
#    raw_input()
    print PS.GetAllPerms ()
#    raw_input()
    print PS.GetAllUris()
#    raw_input()
    
if __name__ == '__main__':
    #Main()
    Main (sys.argv[1])