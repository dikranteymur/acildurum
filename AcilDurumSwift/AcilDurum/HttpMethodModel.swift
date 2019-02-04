//
//  HttpMethodModel.swift
//  AcilDurum
//
//  Created by Dikran Teymur on 30.01.2019.
//  Copyright © 2019 mdt. All rights reserved.
//

import Foundation
import UIKit

public class HttpMethod {
    
    
    func jsonPost(username: String, password: String, url: String) {
        let userJson = ["username": username, "password": password]
        
        let jsonData = try? JSONSerialization.data(withJSONObject: userJson, options: .sortedKeys)
        let url = URL(string: url)
        var request = URLRequest(url: url!)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpBody = jsonData
        
        let task = URLSession.shared.dataTask(with: request) { (data, response, err) in
            if err != nil {
                print("Hata var: \(err!)")
                return
            }
       
            if let result = try? JSONSerialization.jsonObject(with: data!, options: .allowFragments)  as? [String: String] {
                print("Result: \(String(describing: result))")
            } else {
                print("Hata: \(String(describing: err))")
            }
            
            
            
        }
        task.resume()
        
        
//        var request = URLRequest(url: url)
//        request.httpMethod = "POST"
//        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
//        let task = URLSession.shared.uploadTask(with: request, from: uploadData) { (data, response, err) in
//            if let err = err {
//                print("Hata: \(err)")
//                return
//            }
//            guard let response = response as? HTTPURLResponse, (200 ... 500).contains(response.statusCode) else {
//                print("Server Hatasi")
//                return
//            }
//            if let mimeType = response.mimeType, mimeType == "application/json", let data = data, let dataString = String(data: data, encoding: .utf8) {
//                print("Hata: \(dataString)")
//            }
//        }
//        print(task)
//        task.resume()
        
    }
}
