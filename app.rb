require 'rubygems'
require 'sinatra'

get '/' do
  erb 'hello world'
end

post '/convert' do
  redirect to '/'
end
