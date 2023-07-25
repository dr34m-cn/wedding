<template>
	<view class="page0">
		<pHeng size="24" top="96" margin="315"></pHeng>
		<view class="img0"></view>
		<view class="text" v-html="vuex_text2">
			
		</view>
		<view class="linTxt">
			<xBtn lText="新娘" rText="姜海兰" type="1"></xBtn>
			<view class="circlePhoto pt2"></view>
		</view>
		<view class="linTxt">
			<view class="circlePhoto pt1"></view>
			<xBtn lText="新郎" rText="王启航" type="1"></xBtn>
		</view>
		<view class="text" v-html="vuex_text3"></view>
		<view class="flim">
			<image :src="flim" class="flimBorder"></image>
		</view>
	</view>
</template>

<script>
	import pHeng from '@/pages/components/utils/pHeng.vue';
	import xBtn from '@/pages/components/utils/xBtn.vue';
	export default {
		components: {
			pHeng,
			xBtn
		},
		name: 'page0',
		data() {
			return {
				flim: require('@/static/flim.png')
			}
		},
		methods: {}
	}
</script>

<style lang="scss">
	.page0 {
		.img0 {
			width: 594rpx;
			height: 831rpx;
			margin: 77rpx;
			background-image: url($url+'02.jpg');
			background-position: center;
			background-size: 700rpx auto;
		}

		.text {
			text-align: center;
			color: #cebdb5;
			margin: 80rpx 0;
		}

		.linTxt {
			display: flex;
			align-items: center;
			justify-content: center;
			margin: 36rpx 0;

			.circlePhoto {
				width: 260rpx;
				height: 260rpx;
				border-radius: 50%;
			}

			.pt1 {
				margin-right: 50rpx;
				background-image: url($url+'03.jpg');
				background-position: 370rpx 580rpx;
				background-size: 520rpx auto;
			}

			.pt2 {
				margin-left: 80rpx;
				background-image: url($url+'04.jpg');
				background-position: -120rpx 550rpx;
				background-size: 490rpx auto;
			}
		}

		.flim {
			background-image: url($url+'05.jpg');
			background-position: center;
			background-size: 650rpx auto;
			width: 670rpx;
			height: 448rpx;
			margin: 0 40rpx;

			.flimBorder {
				width: 670rpx;
				height: 450rpx;
			}
		}
	}
</style>