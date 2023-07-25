<template>
	<view class="page1">
		<sLine style="margin-top: 40rpx;"></sLine>
		<template v-for="(item,index) in chapter">
			<chapter :data="item" :index="index + 1"></chapter>
		</template>
	</view>
</template>

<script>
	import sLine from '@/pages/components/utils/sLine.vue';
	import chapter from '@/pages/components/utils/chapter.vue';
	export default {
		name: 'page1',
		components: {
			sLine,
			chapter
		},
		data() {
			return {
				chapter: [{
					title: "相遇",
					content: "我野蛮生长<br/>没能成为自己的月亮<br/><br/>能遇见你<br/>是银河赠送我的糖",
					ptSmall: '41',
					ptBig: '42',
					ptBottom: '43'
				}, {
					title: "相知",
					content: "过去的很长时间<br/>都觉得世界对我太不公平<br/>让我饱受质疑，吃尽苦头<br/><br/>现在看来<br/>一切痛苦都是为了更好的快乐<br/>所有不幸的终点，都是幸福<br/><br/>幸福变得可以感受<br/>比如，你抱着我的时候",
					ptSmall: '44',
					ptBig: '45',
					ptBottom: '46'
				},{
					title: "相恋",
					content: "2018/03/25<br/><br/>我要和你谈谈<br/>不灭的鬼怪与神论<br/>人间的烟火与朝阳<br/>三月份的第四个周末<br/>和一场很久的恋爱",
					ptSmall: '47',
					ptBig: '48',
					ptBottom: '49'
				}, {
					title: "相伴",
					content: "这颗蓝色的星球<br/>又在该恒星系里完成了一次公转<br/>很开心今年也和您一起进行<br/>这九亿四千万公里的星际旅行<br/>旅行秒速29.78公里 93马赫<br/>希望明年依旧和您一起看热闹世界",
					ptSmall: '50',
					ptBig: '51',
					ptBottom: '52'
				}, {
					title: "嘉姻",
					content: "春天是一张春饼两泡新茶<br/>夏天是三瓶雪花四块西瓜<br/>秋天是五颗栗子六朵桂花<br/>冬天是七块年糕八个地瓜<br/><br/>春夏秋冬是四季<br/>四季是一生<br/>一生是和你一起慢慢熬白的<br/>满头银发",
					ptSmall: '53',
					ptBig: '54',
					ptBottom: '55'
				}]
			}
		},
		methods: {}
	}
</script>

<style lang="scss">
	.page1 {}
</style>