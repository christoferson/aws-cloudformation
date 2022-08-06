package com.demo.lambda;

import java.util.List;
/*
import com.amazonaws.services.rds.AmazonRDS;
import com.amazonaws.services.rds.AmazonRDSClientBuilder;

import com.amazonaws.services.rds.model.DBInstance;
import com.amazonaws.services.rds.model.DescribeDBInstancesRequest;
import com.amazonaws.services.rds.model.DescribeDBInstancesResult;
*/
public class DemoSdkRds {

    public static String demo() {
    	
    	String instanceIdentifier = System.getenv("CUSTOM_DB_INSTANCE_ID");
    	
    	if (instanceIdentifier == null) {
    		return "DemoSdkRds - Environment CUSTOM_DB_INSTANCE_ID not specified.";
    	}
    	/*
    	AmazonRDS client = AmazonRDSClientBuilder.standard()
				  //.credentialsProvider(credentialsProvider)
				  //.region(region)
				  .build();
    	
    	instanceDescribe(client, instanceIdentifier);
    	*/
    	return "DemoSdkRds";
    	
    }
/*    
	public static void instanceDescribe(AmazonRDS client, String instanceIdentifier) {

    	System.out.printf("Describe Database Instance ... %n");
    	
		DescribeDBInstancesRequest request = new DescribeDBInstancesRequest();
		request.setDBInstanceIdentifier(instanceIdentifier);
		
		DescribeDBInstancesResult result = client.describeDBInstances(request);
		
		List<DBInstance> elements = result.getDBInstances();
        for (DBInstance element : elements) {
            System.out.println(String.format("Arn=%s %n  Name=%s Status=%s", element.getDBInstanceArn(), element.getDBName(), element.getDBInstanceStatus()));
        }
        
	}    
*/
}