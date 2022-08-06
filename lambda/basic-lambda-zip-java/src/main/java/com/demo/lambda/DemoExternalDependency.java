package com.demo.lambda;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.core.JsonProcessingException;

public class DemoExternalDependency {

    public static String demo() {
    
    	ObjectMapper mapper = new ObjectMapper();

        Foo foo = new Foo("Nimbus", "Dark Cotton");
        String jsonStr = null;
        
        try {
        	jsonStr = mapper.writeValueAsString(foo);
        } catch (JsonProcessingException e) {
        	throw new RuntimeException(e);
        }
        
        return jsonStr;
        
    }
	
	public static class Foo {
		
		private String name;
		
		private String description;
		
		public Foo(String name, String description) {
			this.name = name;
			this.description = description;
		}
		
		public String getName() {
			return name;
		}
		
		public void setName(String name) {
			this.name = name;
		}
		
		public String getDescription() {
			return description;
		}
		
		public void setDescription(String description) {
			this.description = description;
		}
		
		public String toString() {
			return String.format("Name=%s Description=%s", name, description);
		}
		
	}

}