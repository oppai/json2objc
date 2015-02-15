require './app/json2dict'

describe Json2Dict do
  it 'recieve Json String or Dictionary String' do
    expect(Json2Dict.new("{'fruits':['apple','banana','melon']}")).not_to eq nil
    expect(Json2Dict.new('@{@"fruits":@[@"apple",@"banana",@"melon"]}')).not_to eq nil 
  end
  it 'dont recieve not Json String or not Dictionary String' do
  end
end
