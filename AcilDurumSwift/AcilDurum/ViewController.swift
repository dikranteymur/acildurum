//
//  ViewController.swift
//  AcilDurum
//
//  Created by Dikran Teymur on 28.01.2019.
//  Copyright © 2019 mdt. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var usernameTextField: UITextField!
    @IBOutlet weak var passwordTextField: UITextField!
    @IBOutlet weak var mesajLabel: UILabel!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    @IBAction func registerButton(_ sender: Any) {
        let url = "http://127.0.0.1:5000/register"
        let username = usernameTextField.text ?? ""
        let password = passwordTextField.text ?? ""
        jsonPost(username: username, password: password, url: url)
        
    }
    
    
    @IBAction func loginButton(_ sender: Any) {
        let url = "http://127.0.0.1:5000/login"
        let username = usernameTextField.text ?? ""
        let password = passwordTextField.text ?? ""
        jsonPost(username: username, password: password, url: url)
        
    }
    
    
    
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
                DispatchQueue.main.async {
                    
                    self.mesajLabel.text = "Hata!!!"
                    
                }
                
                print("Hata var: \(err!)")
                return
            }
            
            
            if let jsonResult = try? JSONSerialization.jsonObject(with: data!, options: .mutableContainers) as? Dictionary<String, Any> {
                DispatchQueue.main.async {
                    self.mesajLabel.text = (jsonResult!["mesaj"] as! String)
                }
            }
        }
        task.resume()
    }
}

