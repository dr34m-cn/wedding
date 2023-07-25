<template>
	<view class="xBtn">
		<view class="left type1" v-if="type == '1'">{{lText}}</view>
		<view class="left type2" v-else>{{lText}}</view>
		<view class="right">
			<view class="sln"></view>
			<view class="txt-content">{{rText}}</view>
		</view>
	</view>
</template>

<script>
	export default {
		props: ["lText","rText","type"],
		name: 'xBtn',
		data() {
			return {}
		},
		methods: {}
	}
</script>

<style lang="scss">
	.xBtn {
		display: flex;
		justify-content: flex-start;
		align-items: flex-end;
		
		.left {
			margin-right: -36rpx;
			padding-bottom: 50rpx;
		}
		
		.type1 {
			color: #957870;
			font-size: 30rpx;
		}
		
		.type2 {
			font-size: 38rpx;
			font-weight: bold;
			color: #FFFFFF;
		}
		
		.right {
			display: flex;

			.sln {
				transform: rotate(50deg);
				height: 90rpx;
				border-left: 2rpx solid #655043;
				margin-top: -38rpx;
				margin-left: 60rpx;
				margin-right: -10rpx;
			}

			.txt-content {
				display: flex;
				align-items: center;
				justify-content: center;
				height: 56rpx;
				color: #7a6760;
				font-size: 26rpx;
				padding: 0 46rpx;
				background-color: #e1c0a1;
			}
		}
	}
</style>