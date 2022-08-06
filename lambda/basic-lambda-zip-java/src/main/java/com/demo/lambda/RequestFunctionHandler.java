package com.demo.lambda;

import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

import java.math.BigDecimal;
import java.util.Map;
import java.util.logging.Logger;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.core.JsonProcessingException;

public class RequestFunctionHandler implements RequestHandler<Map<String,String>, String> {

    private static final Logger LOGGER = Logger.getLogger(RequestFunctionHandler.class.getName());

    public String handleRequest(Map<String, String> values, Context context) {

        LOGGER.info("Start: " + values);
        
        String jsonStr = DemoExternalDependency.demo();
        
        return jsonStr;
        
    }

}