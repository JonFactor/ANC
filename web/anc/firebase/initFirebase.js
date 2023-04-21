// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getFirestore, collection, getDocs } from 'firebase/firestore'
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
export default function pull() {
    const firebaseConfig = {
        apiKey: "AIzaSyBUgpZ303GwAWNENJDdzmiMkDzjsUUYef8",
        authDomain: "scraper-4e219.firebaseapp.com",
        projectId: "scraper-4e219",
        storageBucket: "scraper-4e219.appspot.com",
        messagingSenderId: "944647202457",
        appId: "1:944647202457:web:26cc8d8926b7f1274bfa08",
        measurementId: "G-5LN5576C7P"
        };
    
        // Initialize Firebase
        initializeApp(firebaseConfig);
    
        // init services
        const db = getFirestore()
    
        // collection ref
        const ref = collection(db, 'starting')
        // get collection ref
        let data2
        getDocs(ref)
            .then((snapshot) =>{
                let data1 = []
                snapshot.docs.forEach((doc) =>{
                    data1.push({ ...doc.data(), id:doc.id })
                })
                data2 = data
            }) // when complete    
            .catch(err =>{
                console.log(err.message)
            })
            
        return data2
}