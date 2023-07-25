<template>
	<view class="chapter">
		<view class="title">
			<template v-if="index % 2 == 1">
				<pZong size="20" class="pZon"></pZong>
				<xBtn :lText="'Chapter '+index" :rText="data.title" type="2"></xBtn>
			</template>
			<template v-else>
				<xBtn :lText="'Chapter '+index" :rText="data.title" type="2"></xBtn>
				<pZong size="20" class="pZon2"></pZong>
			</template>
		</view>
		<view class="center">
			<template v-if="index % 2 == 1">
				<view class="btmBox">
					<view class="lin linL"></view>
					<view class="txt txtL">
						Love is the beauty<br />of the soul
					</view>
				</view>
				<view class="pt1 left" :style="'background-image: url(' + vuex_url + 'photo/' + data.ptSmall + '.png);'" />
				<view class="pt2" :style="'background-image: url(' + vuex_url + 'photo/' + data.ptBig + '.png);'" />
			</template>
			<template v-else>
				<view class="btmBox">
					<view class="lin linR"></view>
					<view class="txt txtR">
						Love is the beauty<br />of the soul
					</view>
				</view>
				<view class="pt2 left" :style="'background-image: url(' + vuex_url + 'photo/' + data.ptBig + '.png);'" />
				<view class="pt1" :style="'background-image: url(' + vuex_url + 'photo/' + data.ptSmall + '.png);'" />
			</template>
		</view>

		<view class="content" v-html="data.content"></view>
		<view class="pt3" :style="'background-image: url(' + vuex_url + 'photo/' + data.ptBottom + '.png);'" />
	</view>
</template>

<script>
	import pZong from '@/pages/components/utils/pZong.vue';
	import xBtn from '@/pages/components/utils/xBtn.vue';
	export default {
		props: ['data', 'index'],
		name: 'chapter',
		components: {
			pZong,
			xBtn
		},
		data() {
			return {}
		},
		methods: {}
	}
</script>

<style lang="scss">
	.chapter {
		.title {
			display: flex;
			align-items: center;
			justify-content: center;
			margin-top: 60rpx;

			.pZon {
				margin-right: 40rpx;
				padding-bottom: 40rpx;
			}

			.pZon2 {
				margin-left: 40rpx;
			}
		}

		.center {
			margin: 80rpx 50rpx;
			display: flex;
			align-items: center;
			position: relative;

			.btmBox {
				position: absolute;
				top: 420rpx;

				.lin {
					width: 285rpx;
					height: 2rpx;
					background-color: #e1c0a1;
					margin-bottom: 20rpx;
					z-index: 20;
				}

				.txt {
					color: #876c64;
				}

				.linL {
					margin-left: 100rpx;
				}

				.txtL {
					margin-left: -20rpx;
				}

				.linR {
					margin-left: 260rpx;
				}

				.txtR {
					margin-right: -130rpx;
					text-align: right;
				}
			}

			.pt1 {
				width: 242rpx;
				height: 347rpx;
				margin-bottom: 80rpx;
				background-size: 242rpx 347rpx;
			}

			.left {
				margin-right: 80rpx;
			}

			.pt2 {
				width: 336rpx;
				height: 505rpx;
				background-size: 336rpx 505rpx;
			}
		}

		.content {
			padding-left: 72rpx;
		}

		.pt3 {
			width: 630rpx;
			height: 400rpx;
			background-size: 630rpx 400rpx;
			margin: 80rpx 60rpx;
		}
	}
</style>