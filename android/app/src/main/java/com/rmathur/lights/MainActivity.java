package com.rmathur.lights;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.util.Log;

import com.android.volley.Request;
import com.android.volley.RequestQueue;
import com.android.volley.Response;
import com.android.volley.VolleyError;
import com.android.volley.toolbox.StringRequest;
import com.android.volley.toolbox.Volley;
import com.llollox.androidtoggleswitch.widgets.ToggleSwitch;

import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity {

    final String URL_LIGHTS_ON = "http://192.168.0.21:5000/on";
    final String URL_LIGHTS_OFF = "http://192.168.0.21:5000/off";
    final String URL_LIGHTS_STATUS = "http://192.168.0.21:5000/status";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        //
        // Initialize the Volley queue.
        //

        final RequestQueue queue = Volley.newRequestQueue(this);

        //
        // Initialize UI elements.
        //

        setContentView(R.layout.activity_main);

        final ToggleSwitch toggleSwitch = (ToggleSwitch) findViewById(R.id.light_status_switch);
        toggleSwitch.setOnChangeListener(new ToggleSwitch.OnChangeListener(){
            @Override
            public void onToggleSwitchChanged(int position) {
                StringRequest stringRequest;
                switch (position) {
                    case 0:
                        stringRequest = new StringRequest(Request.Method.GET, URL_LIGHTS_OFF,
                                new Response.Listener<String>() {
                                    @Override
                                    public void onResponse(String response) {
                                        // nothing
                                    }
                                }, new Response.ErrorListener() {
                            @Override
                            public void onErrorResponse(VolleyError error) {
                                // TODO: error here
                                Log.e("Lights", error.getMessage());
                            }
                        });

                        queue.add(stringRequest);
                        break;
                    case 1:
                        stringRequest = new StringRequest(Request.Method.GET, URL_LIGHTS_ON,
                                new Response.Listener<String>() {
                                    @Override
                                    public void onResponse(String response) {
                                        // nothing
                                    }
                                }, new Response.ErrorListener() {
                            @Override
                            public void onErrorResponse(VolleyError error) {
                                // TODO: error here
                                Log.e("Lights", error.getMessage());
                            }
                        });

                        queue.add(stringRequest);
                        break;
                    default:
                        break;
                }
            }
        });

        //
        // Initialize switch state using light state.
        //

        StringRequest stringRequest = new StringRequest(Request.Method.GET, URL_LIGHTS_STATUS,
                new Response.Listener<String>() {
                    @Override
                    public void onResponse(String response) {

                        //
                        // Update the switch with the current state.
                        //

                        Log.d("Lights", response);

                        try {
                            JSONObject jObject = new JSONObject(response);
                            boolean lightStatus = jObject.getBoolean("status");

                            if (lightStatus) {
                                toggleSwitch.setCheckedPosition(1);
                            } else {
                                toggleSwitch.setCheckedPosition(0);
                            }
                        } catch (JSONException exception) {

                        }

                    }
                }, new Response.ErrorListener() {
            @Override
            public void onErrorResponse(VolleyError error) {
                // TODO: error here
                Log.e("Lights", error.getMessage());
            }
        });

        queue.add(stringRequest);
    }
}
