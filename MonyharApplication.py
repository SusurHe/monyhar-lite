
from os import readlink
import webbrowser
import json
import time
from tqdm import tqdm
'''
配置参数:
    homepage: 浏览器首页地址(默认为梦弘搜索器)
'''

# Test request

HOMEPAGE = 'https://so.monyhar.top/'

def icon():
    icon = '''
                                 \....\                              
                      \#+++++++++++++++++\                       
                   \++++++++++++++++++++++++.                    
                .#+++++++++++++++++++++++++++++#$                
              #+++++++++++++++++++++++++++++++++++$              
            \++++++++++++++++++++++++++++++++++++++#             
            #++++++++++++++++++++++++++++++++++++++++            
             +++++++++++++++++++++++++++++++++++++++++\          
        $\    #++++++++++++++++++++++++++++++++++++++++.         
       $##     +++++++++++++++++++++++++++++++++++++++++#        
      $####     ++++++++++++#\\$                                 
      ######     ++++++++.                                       
     .######\    $+++++#                                         
     ########.     ++#      +-------$     $$$$$$$$$$$$$$$$$      
    \#########.     +     +----------+     $$$$$$$$$$$$$$$$$     
    .##########.    $    -------------+     $$$$$$$$$$$$$$$$     
    ############\       #--------------.    $$$$$$$$$$$$$$$$     
    #############$      ----------------    $$$$$$$$$$$$$$$$     
    ##############\     ----------------    $$$$$$$$$$$$$$$$     
    ###############\    #--------------.    $$$$$$$$$$$$$$$$     
    .###############     -------------+     $$$$$$$$$$$$$$$$     
     ################     #----------+     $$$$$$$$$$$$$$$$$     
     ################.      +-------      $$$$$$$$$$$$$$$$$      
     $#################.                 $$$$$$$$$$$$$$$$$$      
      ###################.              $$$$$$$$$$$$$$$$$$       
       ######################\$$$$     $$$$$$$$$$$$$$$$$$        
        #########################\    $$$$$$$$$$$$$$$$$$$        
         #######################\    $$$$$$$$$$$$$$$$$$$         
          .####################\    $$$$$$$$$$$$$$$$$$           
           \##################.     $$$$$$$$$$$$$$$$$            
             ################.     $$$$$$$$$$$$$$$$$             
              $#############.     $$$$$$$$$$$$$$$$               
                $.##########     $$$$$$$$$$$$$$$                 
                    .######     $$$$$$$$$$$$                     
                       $\#$    $$$$$$$$$$                        
                                                                 
                                                                 

------------------ M   O   N   Y   H   A   R ---------------- v0.🐒🐒🐒   
    '''
    print(icon)

# 加载配置文件
def getConfig():
    global HOMEPAGE
    with open('config/config.json', 'r') as f:
        monyharConfig = json.load(f)
    HOMEPAGE = monyharConfig['homepage']
       
# 主程序
def main():
    icon()
    getConfig()
    try:
        webbrowser.open(HOMEPAGE, new=1, autoraise=True)
    except:
        print('Failed connected to the Internet!')
        print('Start retrying now...')
        main()
    else:
        print('Successfully connected to the Internet!')
    
if __name__ == "__main__":
    main()
    with tqdm(total=100) as pbar:
        pbar.set_description('Processing: ')
        for i in range(20):
            time.sleep(0.05)
            pbar.update(10)

