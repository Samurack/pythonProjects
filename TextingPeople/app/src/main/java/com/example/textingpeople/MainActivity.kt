package com.example.textingpeople

import android.Manifest
import android.telephony.SmsManager
import android.widget.Toast

import android.app.Activity
import android.content.Intent
import android.content.SharedPreferences
import android.content.pm.PackageManager
import android.support.v4.app.ActivityCompat
import android.support.v4.content.ContextCompat
import android.support.v7.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText

public class textingContacts extends AppCompatActivity {
    String message;
    String txtphoneNo;
    String phoneNo;

    private static final int MY_PERMISSIONS_REQUEST_SEND_SMS = 0;

    /**
     * use this method to launch the sub-Activity, and provide a
     * functor to handle the result - ok or cancel
     */
    @Override
    protected void onCreate(Bundle savedInstanceState) {

        super.onCreate(savedInstanceState);
        SharedPreferences sharedPreferences = getSharedPreferences ("MyData", MODE_PRIVATE);
        message = "Hey Hows it going?";

        if (ContextCompat.checkSelfPermission(this, Manifest.permission.SEND_SMS) != PackageManager.PERMISSION_GRANTED) {
            if (ActivityCompat.shouldShowRequestPermissionRationale(this, Manifest.permission.SEND_SMS)) {
            } else {
                ActivityCompat.requestPermissions(this, new String []{ Manifest.permission.SEND_SMS }, MY_PERMISSIONS_REQUEST_SEND_SMS);
            }
        } else {
            for (int i = 0; i < 4; i++) {

                txtphoneNo = sharedPreferences.getString(i + "Number", "");
                phoneNo = txtphoneNo;
                if (phoneNo != "") {
                    SmsManager smsManager = SmsManager . getDefault ();
                    smsManager.sendTextMessage(phoneNo, null, message, null, null);
                    Toast.makeText(getApplicationContext(), "SMS sent.", Toast.LENGTH_LONG).show();
                }
            }
        }
    }
}
