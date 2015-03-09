
/** access_token indexes **/
db.getCollection("access_token").ensureIndex({
  "_id": NumberInt(1)
},[
  
]);

/** colleges indexes **/
db.getCollection("colleges").ensureIndex({
  "_id": NumberInt(1)
},[
  
]);

/** friends indexes **/
db.getCollection("friends").ensureIndex({
  "_id": NumberInt(1)
},[
  
]);

/** messages indexes **/
db.getCollection("messages").ensureIndex({
  "_id": NumberInt(1)
},[
  
]);

/** tags indexes **/
db.getCollection("tags").ensureIndex({
  "_id": NumberInt(1)
},[
  
]);

/** users indexes **/
db.getCollection("users").ensureIndex({
  "_id": NumberInt(1)
},[
  
]);

/** userstatus indexes **/
db.getCollection("userstatus").ensureIndex({
  "_id": NumberInt(1)
},[
  
]);

/** whatsup indexes **/
db.getCollection("whatsup").ensureIndex({
  "_id": NumberInt(1)
},[
  
]);

/** access_token records **/
db.getCollection("access_token").insert({
  "_id": ObjectId("54f312edb356410e2b26b4e6"),
  "token": "735cb80103da47dea28764dac643c274",
  "wefriendsid": "testuser",
  "expires": NumberLong(1427808237)
});
db.getCollection("access_token").insert({
  "_id": ObjectId("54fbfca1b3564114643ce1d0"),
  "token": "4ead422735941e703879d12f7562dd93",
  "wefriendsid": "hello",
  "expires": NumberLong(1428392353)
});
db.getCollection("access_token").insert({
  "_id": ObjectId("54fc0458b356411b292ed0c3"),
  "token": "dfc094e75c1edc52ac81d5187b892e7f",
  "wefriendsid": "world",
  "expires": NumberLong(1428394328)
});

/** colleges records **/
db.getCollection("colleges").insert({
  "_id": ObjectId("54d8f2b4678daed7798b4567"),
  "collegeid": "uestc",
  "collegename": "%E7%94%B5%E5%AD%90%E7%A7%91%E6%8A%80%E5%A4%A7%E5%AD%A6"
});

/** friends records **/
db.getCollection("friends").insert({
  "_id": ObjectId("54d8f8b1b356417f8c901dc8"),
  "wefriendsid": "testuser",
  "friends": [
    {
      "wefriendsid": "hello",
      "friendgroup": "myfriends"
    },
    {
      "wefriendsid": "hehehe",
      "friendgroup": "newgroup"
    },
    {
      "wefriendsid": "world",
      "friendgroup": "myfriends"
    }
  ]
});

/** messages records **/
db.getCollection("messages").insert({
  "_id": ObjectId("54fc02fbb35641184558428f"),
  "sender": "hello",
  "receivers": [
    "testuser",
    "world"
  ],
  "message": "helloworld",
  "timestramp": NumberLong(1425801979),
  "messagetype": "text",
  "chatgroup": "",
  "ishandled": [
    "world",
    "testuser"
  ]
});

/** system.indexes records **/
db.getCollection("system.indexes").insert({
  "v": NumberInt(1),
  "key": {
    "_id": NumberInt(1)
  },
  "name": "_id_",
  "ns": "wefriends.colleges"
});
db.getCollection("system.indexes").insert({
  "v": NumberInt(1),
  "key": {
    "_id": NumberInt(1)
  },
  "name": "_id_",
  "ns": "wefriends.users"
});
db.getCollection("system.indexes").insert({
  "v": NumberInt(1),
  "key": {
    "_id": NumberInt(1)
  },
  "name": "_id_",
  "ns": "wefriends.friends"
});
db.getCollection("system.indexes").insert({
  "v": NumberInt(1),
  "key": {
    "_id": NumberInt(1)
  },
  "name": "_id_",
  "ns": "wefriends.tags"
});
db.getCollection("system.indexes").insert({
  "v": NumberInt(1),
  "key": {
    "_id": NumberInt(1)
  },
  "name": "_id_",
  "ns": "wefriends.whatsup"
});
db.getCollection("system.indexes").insert({
  "v": NumberInt(1),
  "key": {
    "_id": NumberInt(1)
  },
  "name": "_id_",
  "ns": "wefriends.access_token"
});
db.getCollection("system.indexes").insert({
  "v": NumberInt(1),
  "key": {
    "_id": NumberInt(1)
  },
  "name": "_id_",
  "ns": "wefriends.userstatus"
});
db.getCollection("system.indexes").insert({
  "v": NumberInt(1),
  "key": {
    "_id": NumberInt(1)
  },
  "name": "_id_",
  "ns": "wefriends.messages"
});

/** tags records **/
db.getCollection("tags").insert({
  "_id": ObjectId("54d8f8b1b356417f8c901dc9"),
  "wefriendsid": "testuser",
  "tags": [
    
  ]
});

/** users records **/
db.getCollection("users").insert({
  "_id": ObjectId("54d8f8b1b356417f8c901dc7"),
  "phone": "18617367382",
  "password": "098f6bcd4621d373cade4e832627b4f6",
  "gender": NumberInt(0),
  "wefriendsid": "testuser",
  "nickname": "%E6%B5%8B%E8%AF%95",
  "region": "Guangzhou",
  "registertime": NumberLong(1423505585),
  "collegeid": "uestc",
  "email": "805432537%40qq.com",
  "avatar": "static%2Favatars%2Fdefault.png",
  "intro": "HelloThere!"
});
db.getCollection("users").insert({
  "_id": ObjectId("54e85b9a678daefc058b4567"),
  "phone": "001",
  "password": "098f6bcd4621d373cade4e832627b4f6",
  "gender": NumberLong(0),
  "wefriendsid": "hello",
  "nickname": "ThisIsHello",
  "region": "Guangzhou",
  "registertime": NumberLong(1423505585),
  "collegeid": "uestc",
  "email": "111%40qq.com",
  "avatar": "static%2Favatars%2Fdefault.png",
  "intro": "HelloThere!"
});
db.getCollection("users").insert({
  "_id": ObjectId("54e85bce678dae9b138b4567"),
  "phone": "001",
  "password": "098f6bcd4621d373cade4e832627b4f6",
  "gender": NumberLong(0),
  "wefriendsid": "world",
  "nickname": "ThisIsWorld",
  "region": "Guangzhou",
  "registertime": NumberLong(1423505585),
  "collegeid": "uestc",
  "email": "222%40qq.com",
  "avatar": "static%2Favatars%2Fdefault.png",
  "intro": "HelloThere!"
});
db.getCollection("users").insert({
  "_id": ObjectId("54fae5ed678dae25068b4567"),
  "phone": "003",
  "password": "098f6bcd4621d373cade4e832627b4f6",
  "gender": NumberLong(0),
  "wefriendsid": "hehehe",
  "nickname": "ThisIsHehehe",
  "region": "Guangzhou",
  "registertime": NumberLong(1423505585),
  "collegeid": "uestc",
  "email": "222%40qq.com",
  "avatar": "static%2Favatars%2Fdefault.png",
  "intro": "HelloThere!"
});

/** userstatus records **/
db.getCollection("userstatus").insert({
  "_id": ObjectId("54ec7a10678dae680ee47328"),
  "wefriendsid": "world",
  "status": "offline"
});
db.getCollection("userstatus").insert({
  "_id": ObjectId("54ec7a10678dae680ee47329"),
  "wefriendsid": "hello",
  "status": "online"
});
db.getCollection("userstatus").insert({
  "_id": ObjectId("54ec7a10678dae680ee4732a"),
  "wefriendsid": "test",
  "status": "online"
});

/** whatsup records **/
db.getCollection("whatsup").insert({
  "_id": ObjectId("54d8f8b1b356417f8c901dca"),
  "wefriendsid": "testuser",
  "whatsup": "%E4%B9%88%E4%B9%88%E5%93%92"
});
db.getCollection("whatsup").insert({
  "_id": ObjectId("54e8610e678daefc058b4568"),
  "wefriendsid": "hello",
  "whatsup": "HeyDude"
});
db.getCollection("whatsup").insert({
  "_id": ObjectId("54e86120678dae9c138b4567"),
  "wefriendsid": "world",
  "whatsup": "GodDamnIt"
});
db.getCollection("whatsup").insert({
  "_id": ObjectId("54fae683678dae0b7f8b4567"),
  "wefriendsid": "hehehe",
  "whatsup": "GodDamnIt"
});
