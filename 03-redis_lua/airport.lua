if tonumber(KEYS[1]) <= 80 and tonumber(KEYS[1]) >= 1 then
  if redis.call("EXISTS", KEYS[1]) == 1 then
    local payload = redis.call("GET", KEYS[1])
    return payload
  else
    redis.replicate_commands()
    local parking_space = math.random(99)
    redis.call("SET",KEYS[1], parking_space)
    return parking_space
  end
end
