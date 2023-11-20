<template>
  <div id="welcomePage" style="margin-bottom:0 ;">
    <div class="bg">
	    <p class="shine">无人做你的光芒?<br/>请自己照亮前方</p>
    	<div id="enter">
        	<router-link to="/login" style="text-decoration: none; color: inherit;"> 
				<el-button color="none" id="enterbutton" style="font-size: 0.6cm;">进入订票系统</el-button> 
			</router-link>
		</div>
	</div>
  </div>
</template>

<script lang="ts" setup>
const myHover = () => {
	
}
</script>

<style>
  #enter {
    margin-top: 150px;
    text-align: center;
  }

  #enterbutton {
    width: 250px;
    height: 70px;
    border-radius: 50px;
	border-width: 2px;
	background-color:#0000;
  }

  #welcomePage {
    background: url("../assets/夏生1.png");
    height: 100vh;
    width: 100vw;
    background-size: cover;
    background-position: center center;
  }

  	.bg{
	    background: #0000; /*设置元素背景颜色*/
	    width: 1000px; /*设置元素宽度*/
	    height: 300px; /*设置元素高度*/
	    margin: 0 auto; /*设置元素外边距*/
	    padding-top: 50px; /*设置元素上内边距*/
	}
	.shine{
	    width: 1000px;
	    font-family: "Microsoft YaHei";
	    font-size: 60px;
	    text-align: center;
	    background: -webkit-linear-gradient(left, rgb(255, 183, 0), rgb(0, 234, 255)) 0 0 no-repeat;/*设置线性渐变*/
	    -webkit-background-size: 250px;                        /*设置背景大小*/
	    -webkit-background-clip: text;                            /*背景被裁剪到文字*/
	    -webkit-text-fill-color: rgba(169, 169, 169, 0.3);        /*设置文字的填充颜色*/
	    -webkit-animation: shine 5s infinite;                    /*设置动画*/
	}
	@-webkit-keyframes shine{   /*创建动画*/
	    0%{
	        background-position: 0 0;
	    }
	    100%{
	        background-position: 100% 100%;
	    }
	}

  </style>