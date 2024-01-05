import Mock from 'mockjs'
//Mock.setup({timeout:5000})

Mock.mock("http://localhost:8081/PaChong",{
    "content":[
        {
            "touch": 538776,
            "videolike": 21185,
            "videocoin": 1322,
            
        }
    
    ]
})