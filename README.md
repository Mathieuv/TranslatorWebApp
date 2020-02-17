# TranslatorWebApp
A simple translation app using google translate Api on Vue

## Run frontend: 
Run main.bat to run the translatorwebapp. 
this will change to the required directory and run npm run dev on localhost:8080

## frontend: 
Contains:
- index.html 
- ./src
- main.js : runs Vue
- App.vue : translator => calls google api for translation
- TODO: dropdown for language selection, import file 
       
## backend:
Contains:
- run.py : in progress 
I was building flask to run api calls.
Had trouble greating a API request and correctly parsing it. 

- translator.py : 
Contains translating function using googletrans package. 

