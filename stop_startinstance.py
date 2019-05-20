import boto3

def lambda_handler(event,context):
    
    # Get list of regions
    ec2_client = boto3.client('ec2')
    
    regions = [region['RegionName'] for region in ec2_client.describe_regions()['Regions']]
    
    for region in regions:
        
        ec2 = boto3.resource('ec2',region_name=region)
        print("Region:",region)
        
        # Stop instances
        
        instances = ec2.instances.filter(Filters=[ {'Name':'instance-state-name','values':['running']}])
        
        
        
        
        for instance in instances:
            instance.stop()
            print('stopped instances:',instance.id)
            
        # start instances
        
        instances = ec2.instances.filter(Filters=[ {'Name':'instance-state-name','values':['stopped']}])
        
        for instance in instances:
            instance.start()
            print('started instances:',instance.id)
