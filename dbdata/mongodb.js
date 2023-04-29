const MongoClient = require('dbdata/mongodb').MongoClient;
const uri = "mongodb://username:password@localhost:27017/?authMechanism=DEFAULT";


MongoClient.connect(uri, function(err, client) {
   if (err) {
      console.error('An error occurred connecting to MongoDB: ', err);
      return;
   }

   const db = client.db("db_project");

   // Employees collection
   db.createCollection("Employees", {
      validator: {
         $jsonSchema: {
            bsonType: "object",
            required: [
               "employeeId",
               "employeeType",
               "firstName",
               "lastName",
               "datOfBirth",
               "email",
               "phone",
               "registerDate",
            ],
            properties: {
               employeeId: { bsonType: "int" },
               employeeType: { bsonType: "string" },
               firstName: { bsonType: "string" },
               lastName: { bsonType: "string" },
               datOfBirth: { bsonType: "date" },
               email: { bsonType: "string" },
               phone: { bsonType: "string" },
               registerDate: { bsonType: "date" },
            },
         },
      },
   });

   // Clients collection
   db.createCollection("Clients", {
      validator: {
         $jsonSchema: {
            bsonType: "object",
            required: [
               "userId",
               "firstName",
               "lastName",
               "datOfBirth",
               "email",
               "phone",
               "address",
               "registerDate",
            ],
            properties: {
               userId: { bsonType: "int" },
               firstName: { bsonType: "string" },
               lastName: { bsonType: "string" },
               datOfBirth: { bsonType: "date" },
               email: { bsonType: "string" },
               phone: { bsonType: "string" },
               address: { bsonType: "string" },
               registerDate: { bsonType: "date" },
            },
         },
      },
   });

   // Games collection
   db.createCollection("Games", {
      validator: {
         $jsonSchema: {
            bsonType: "object",
            required: ["gameId", "gameType", "capacity", "pricePerHour"],
            properties: {
               gameId: { bsonType: "int" },
               gameType: { bsonType: "string" },
               capacity: { bsonType: "int" },
               pricePerHour: { bsonType: "string" },
            },
         },
      },
   });

   // Tables collection
   db.createCollection("Tables", {
      validator: {
         $jsonSchema: {
            bsonType: "object",
            required: ["tableId", "capacity"],
            properties: {
               tableId: { bsonType: "int" },
               capacity: { bsonType: "int" },
            },
         },
      },
   });

   // Reservations collection
   db.createCollection("Reservations", {
      validator: {
         $jsonSchema: {
            bsonType: "object",
            required: [
               "reservationId",
               "reservationStatus",
               "tableId",
               "gameId",
               "peopleCount",
               "startDate",
               "endDate",
            ],
            properties: {
               reservationId: { bsonType: "int" },
               reservationStatus: { bsonType: "string" },
               tableId: { bsonType: "int" },
               gameId: { bsonType: "int" },
               peopleCount: { bsonType: "int" },
               startDate: { bsonType: "date" },
               endDate: { bsonType: "date" },
            },
         },
      },
   });

   // Orders collection
   db.createCollection("Orders", {
      validator: {
         $jsonSchema: {
            bsonType: "object",
            required: ["orderId", "reservationId", "dishes", "orderDate", "finalPrice"],
            properties: {
               orderId: { bsonType: "int" },
               reservationId: { bsonType: "int" },
               dishes: { bsonType: "array", items: { bsonType: "int" } },
               orderDate: { bsonType: "date" },
               finalPrice: { bsonType: "string" },
            },
         },
      },
   });

   // Menu collection
   db.createCollection("Menu", {
      validator: {
         $jsonSchema: {
            bsonType: "object",
            required: ["dishId", "dishType", "description", "dishPrice"],
            properties: {
               dishId: { bsonType: "int" },
               dishType: { bsonType: "string" },
               description: { bsonType: "string" },
               dishPrice: { bsonType: "string" },
            },
         },
      },
   });

   console.log("Collections created!");
   client.close();
});

