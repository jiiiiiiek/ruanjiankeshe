import Mock from 'mockjs'
//Mock.setup({timeout:5000})

Mock.mock("http://localhost:8081/PaChong",{
    "content":[
        {
            "videotitle": '【差评】为什么我敢说，摇一摇广告绝对不会消失？',
            "videotime": '2023-11-24 19:53:18',
            "videoview": 538776,
            "videolike": 21185,
            "videocoin": 1322,
            "videofavorite": 2093,
            "videoshare": 494
        }
    
    ]
})