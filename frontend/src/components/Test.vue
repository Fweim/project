<template>
  <!-- <div class="hello">
    <button type='button' class='btn btn-primary' @click="test_axios">Test</button>
  </div> -->
  <div class="container">
  <div class="row">
    <div class="col-sm-10">
      <h1>Model Cards</h1>
      <hr><br><br>
      <div>
        <vue-tags-input
          v-model="tag"
          :tags="tags"
          :autocomplete-items="filteredItems"
          :add-only-from-autocomplete="true"
          @tags-changed="newTags => tags = newTags"
        />
        <br>
      </div>
      <br><br>
      <table class="table table-hover">
        <thead>
          <tr>
            <th scope="col">Title</th>
            <th scope="col">Tags</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(card,index) in this.model_cards" :key="index">
            <td>{{card.model_details.name}}</td>
            <td></td>
            <td></td>
            <td>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>
</template>

<script>
import VueTagsInput from '@johmun/vue-tags-input'
import axios from 'axios'
//import Vue from 'vue';

export default {
  components: {
    VueTagsInput,
  },
  name: 'HelloWorld',
  data() {
    return {
      model_cards: [],
      filter: [],
      msg2: '',
      search: '',
      filterList: [],
      tag: '',
      tags: [],
      autocompleteItems: []
    }
  },
  props: {
    msg: String,
  },
  methods: {
    test_axios: function () {
      console.log('Hallo Welt')
    },
    test_search: function () {
      //this.filter = this.search
      this.filterList.push(this.search)
      this.search = ''
      console.log(this.filterList)
    },
    handleclick() {
      this.tags.forEach((tag) => {
        console.log(tag.text)
      })
    },
    tagadded(obj) {
      obj.addTag();
    },
    onTest() {
      axios.post('/api/test', {
        msg2: this.tags
      })
      .then(response => {
        console.log(response.data)
      })
    },
    loadTags() {
      for (let i = 0; i < this.model_cards.length; i++){
        //console.log(this.model_cards[i].model_details)
        this.model_cards[i].model_details.citations.forEach((cit) => {
          this.filter.push({"text": cit.citation})
        })
      }
      console.log(this.filter)
      this.removeDuplicates();
    },
    removeDuplicates(){
      var arr = this.filter
      var split = arr

      var uniqueArray = []
      //var uniqueJson = {}
      for (let i = 0; i < split.length; i++){
        if(!uniqueArray.find(x => x.text === split[i].text)){
          uniqueArray.push(split[i])
        }
      }
      console.log(uniqueArray)
      this.autocompleteItems = uniqueArray
    },
    onLoad() {
      axios.get('/api/test_db')
        .then(response => {
          this.model_cards = response.data
          console.log(this.model_cards)
        }).finally(() => {
          this.loadTags();
        })
    }
  },
  computed: {
    filteredItems() {
      return this.autocompleteItems.filter(i => {
        return i.text.toLowerCase().indexOf(this.tag.toLowerCase()) !== -1;
      })
    },
  },
  mounted: function(){
    this.onLoad();
    // this.loadTags();
    // this.removeDuplicates();
  }
}
</script>
<style scoped>
div.flex {
    display: flex;
    gap: 20px;
    margin: 5px;
    padding: 1px;
}
</style>